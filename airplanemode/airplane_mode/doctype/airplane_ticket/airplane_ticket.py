# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document
from frappe.utils import getdate, nowdate
from frappe import _

class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate()
        
        if not self.flight_price:
            frappe.throw("Please provide a flight price.")

        self.apply_dynamic_pricing()

        total_amount = self.flight_price

        if self.add_ons:
            for item in self.add_ons:
                if item.amount:
                    total_amount += item.amount

        self.total_amount = total_amount

    def apply_dynamic_pricing(self):
        if not self.departure_date:
            return
        
        base_price = float(self.flight_price)
        booking_date = getdate(self.booking_date) if self.booking_date else getdate(nowdate())
        flight_date = getdate(self.departure_date)

        days_to_flight = (flight_date - booking_date).days

        if days_to_flight <= 1:
            multiplier = 1.5
        elif days_to_flight <= 3:
            multiplier = 1.3
        elif days_to_flight <= 7:
            multiplier = 1.1
        else:
            multiplier = 1.0

        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        capacity = airplane.capacity

        existing_tickets = frappe.db.count("Airplane Ticket", filters = {"flight" : self.flight})

        if existing_tickets / capacity >= 0.8:
            multiplier += 0.2

        self.flight_price = round(base_price * multiplier, 2)
        

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("The ticket can only be submitted if the status is Boarded.")

    def before_save(self):
        if self.status == "Booked":
            self.status = "Booked"

    def remove_duplicate(self):
        unique_add_ons = {}
        for a in self.add_ons:
            key = a.item
            if key not in unique_add_ons:
                unique_add_ons[key] = a
            else:
                frappe.msgprint(f"The item '{key}' already exists and has been removed.")
        self.set("add_ons", list(unique_add_ons.values()))

    def before_insert(self):
        self.check_flight_capacity()

        if not self.seat:
            self.seat = f"{random.randint(1, 100)}{random.choice('ABCDE')}"

    def check_flight_capacity(self):
        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        capacity = airplane.capacity

        existing_tickets = frappe.db.count("Airplane Ticket", filters ={"flight": self.flight})

        if existing_tickets >= capacity:
            frappe.throw(_("Cannot create a new ticket. The flight has reached its full capacity of {0} seats.").format(capacity)) 

    

    # def on_submit(self):
    #     # self.db.set("status", "Boarded")
    #     self.status = "Boarded"