# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Airline(Document):
    def validate(self):
		
        if self.customer_care:  
            doc_name = frappe.db.exists("Airline", {"customer_care": self.customer_care})
            if doc_name and doc_name != self.name:
                frappe.throw(f"Duplicate entry found with Customer Care Number: {self.customer_care}")
                
	
		# def validate(self):
        #       doc = frappe.get_doc('Airline', 'SK')
        #       print(doc, "-------")
        #       if self.customer_care:
        #               doc_name = frappe.db.exists("Airline", {"customer_care": self.customer_care})
        #               if doc_name and doc_name != self.name:
        #                       frappe.throw(f"Duplicate entry found with Customer Care Number: {self.customer_care}")
          