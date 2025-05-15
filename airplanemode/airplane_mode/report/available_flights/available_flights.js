// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt

frappe.query_reports["Available Flights"] = {
	"filters": [
		{
            fieldname: 'from_date',
            label: __('From Date'),
            fieldtype: 'Date'
        },
        {
            fieldname: 'to_date',
            label: __('To Date'),
            fieldtype: 'Date'
        },
        {
            fieldname: 'airplane',
            label: __('Airplane'),
            fieldtype: 'Link',
            options: 'Airplane'
        }
	]
};
