# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FYYear(Document):
    def validate(self):
        self.check_duplicate_name()

    def check_duplicate_name(self):
        
        if frappe.db.exists({"doctype": "FY Year", "fy_name": self.fy_name}):
            frappe.throw(f"Fiscal Year '{self.fy_name}' already exists.")

        # if frappe.db.exists("FY Year", {"fy_name" : self.fy_name, "name": ["!=", self.name]}):
        #     frappe.throw(f"Fiscal Year '{self.fy_name}' already exists.")