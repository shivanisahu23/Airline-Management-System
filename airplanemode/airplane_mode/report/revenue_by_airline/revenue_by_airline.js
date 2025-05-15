// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt


frappe.query_reports["Revenue by Airline"] = {
	"filters": [
		{
			fieldname: 'from_date',
			label: __('From Date'),
			fieldtype: 'Date',
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			fieldname: 'to_date',
			label: __('To Date'),
			fieldtype: 'Date',
			default: frappe.datetime.get_today()
		},
		{
			fieldname: 'airline',
			label: __('Airline'),
			fieldtype: 'Link',
			options: 'Airline'
		}
	]
}

// frappe.query_reports["Revenue by Airline"] = {
// 	"filters": [
// 		{
// 			fieldname: 'from_date',
// 			label: __('From Date'),
// 			fieldtype: 'Datetime'
// 			// default: frappe.datetime.add_months(frappe.datetimem.get_today(), -1)
// 		},
// 		{
// 			fieldname: 'to_date',
// 			label: __('To Date'),
// 			fieldtype: 'Date'
// 			// default: frappe.datetime.get_today()
// 		},
// 		{
// 			fieldname: 'airline',
// 			label: __('Airline'),
// 			fieldtype: 'Link',
// 			options: 'Airline'
// 		}
// 	]
// }
