# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import get_datetime
from datetime import timedelta
from frappe import _


class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.status = "Completed"

    def get_page_info(self):
        return {
            "published": self.is_published,
        }
    
    def validate(self):
        self.calculate_arrival_time()

        if self.date_of_departure and self.date_of_departure < frappe.utils.nowdate():
            frappe.throw(_("You cannot create a ticket for a flight in the past."))


    def calculate_arrival_time(self):
        if self.date_of_departure and self.time_of_departure and self.duration:
            dt = get_datetime(f"{self.date_of_departure} {self.time_of_departure}")
            dt += timedelta(seconds=self.duration)
            self.date_to_reach = dt.date()
            self.time_to_reach = dt.time()

