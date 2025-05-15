# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FYMonthlyAmount(Document):
	def validate(self):
		self.calculate_total_amount()
		# self.set_month_of_year()

	def calculate_total_amount(self):
		total = 0
		for d in self.table:
			if d.amount:
				total += float(d.amount or 0)
		self.total_amount = total 

	# def set_month_of_year(self):
	# 	if self.month and self.fiscal_year:
	# 		self.month_of_year = f'{self.month} {self.fiscal_year}'









































































































