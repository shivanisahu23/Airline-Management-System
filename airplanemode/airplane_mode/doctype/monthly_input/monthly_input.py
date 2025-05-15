# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyInput(Document):
    pass

@frappe.whitelist()
def get_value(fiscal_year, name1, amount, month):
    fiscal_doc_name = frappe.db.exists("FY Monthly Amount", {"fiscal_year": fiscal_year})
    
    if fiscal_doc_name:
        fiscal_doc = frappe.get_doc("FY Monthly Amount", fiscal_doc_name)
        
        if fiscal_doc.month == month:
            for row in fiscal_doc.table:
                if row.name1 == name1:
                    frappe.throw(f"Duplicate Entry: {name1} already exists for month {month} in fiscal year {fiscal_year}.")

            fiscal_doc.append("table", {
                "name1": name1,
                "amount": amount
            })
            fiscal_doc.save(ignore_permissions=True)
            frappe.msgprint(f"Added {name1} to {month} in fiscal year {fiscal_year}.")
        else:
            fiscal_doc = frappe.new_doc("FY Monthly Amount")
            fiscal_doc.fiscal_year = fiscal_year
            fiscal_doc.month = month
            fiscal_doc.append("table", {
                "name1": name1,
                "amount": amount
            })
            fiscal_doc.save(ignore_permissions=True)
            frappe.msgprint(f"New fiscal year document created for {month} {fiscal_year} and {name1} added.")
    else:
        fiscal_doc = frappe.new_doc("FY Monthly Amount")
        fiscal_doc.fiscal_year = fiscal_year
        fiscal_doc.month = month
        fiscal_doc.append("table", {
            "name1": name1,
            "amount": amount
        })
        fiscal_doc.save(ignore_permissions=True)
        frappe.msgprint(f"New fiscal year document created for {month} {fiscal_year} and {name1} added.")



# # Copyright (c) 2025, Shivani Sahu and contributors
# # For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class MonthlyInput(Document):
#     pass

# @frappe.whitelist()
# def get_value(fiscal_year, name1, amount, month):
#     fiscal_doc_name = frappe.db.exists("FY Monthly Amount", {"fiscal_year": fiscal_year}) # True, False
#     print(f"""\n\n\n\n already exists={fiscal_doc_name}\n\n\n\n""") 
   
#     if fiscal_doc_name:
#         fiscal_doc = frappe.get_doc("FY Monthly Amount", fiscal_doc_name)
#         print(f"""\n\n\n\n already exists fiscal_doc={fiscal_doc_name}\n\n\n\n""") # need to check some python basic  

#         if fiscal_doc.month == month:
#             print(f"""\n\n\n\n fiscal_doc.months={fiscal_doc}, if True\n\n\n\n""")
#             for row in fiscal_doc.table:
#                 if row.name1 == name1:
#                     frappe.throw(f"Duplicate Entry: {name1} already exists for month {month} in fiscal year {fiscal_year}.")

#             fiscal_doc.append("table", {
#                 "name1": name1,
#                 "amount": amount
#             })
#             fiscal_doc.save(ignore_permissions=True)
#             frappe.msgprint(f"Added {name1} to {month} in fiscal year {fiscal_year}.")
#         else:
#             fiscal_doc = frappe.new_doc("FY Monthly Amount")
#             fiscal_doc.fiscal_year = fiscal_year
#             fiscal_doc.month = month
#             fiscal_doc.append("table", {
#                 "name1": name1,
#                 "amount": amount
#             })
#             fiscal_doc.save(ignore_permissions=True)
#             frappe.msgprint(f"New fiscal year document created for {month} {fiscal_year} and {name1} added.")
#     else:
#         print(f"""\n\n\n not fiscal_doc_name={fiscal_doc_name}\n\n\n""")
#         fiscal_doc = frappe.new_doc("FY Monthly Amount")
#         fiscal_doc.fiscal_year = fiscal_year
#         fiscal_doc.month = month
#         fiscal_doc.append("table", {
#             "name1": name1,
#             "amount": amount
#         })
#         fiscal_doc.save(ignore_permissions=True)
#         frappe.msgprint(f"New fiscal year document created for {month} {fiscal_year} and {name1} added.")
