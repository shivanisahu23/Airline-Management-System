// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue by Airline2"] = {
	"filters": [
		{
			field_name: "from_date",
			label: __("From Date"),
			fieldtype: "Date"
		},
		{
			field_name: "to_date",
			label: __("To Date"),
			fieldtype: "Date"
		},
		{
			field_name: "airline",
			label: __("Airline"),
			fieldtype: "Link",
			options: "Airline"
		}
	]
};


// {
// 	fieldname: 'from_date',
// 	label: __('From Date'),
// 	fieldtype: 'Date'
// },
// {
// 	fieldname: 'to_date',
// 	label: __('To Date'),
// 	fieldtype: 'Date'
// },
// {
// 	fieldname: 'airplane',
// 	label: __('Airplane'),
// 	fieldtype: 'Link',
// 	options: 'Airplane'
// }