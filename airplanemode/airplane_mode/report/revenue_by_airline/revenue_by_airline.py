# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate, add_days, today

def get_columns():
    return [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 200
        }
    ]

def execute(filters=None):
    filters = filters or {}
    # conditions = ""
    # values = {}

    # if filters.get("from_date"):
    #     conditions += " AND at.departure_date >= %(from_date)s"
    #     values["from_date"] = filters.get("from_date")

    # if filters.get("to_date"):
    #     conditions += " AND at.departure_date <= %(to_date)s"
    #     values["to_date"] = filters.get("to_date")

    # if filters.get("airline"):
    #     conditions += " AND a.name = %(airline)s"
    #     values["airline"] = filters.get("airline")

    # revennue_data = frappe.db.sql(f"""
    #     SELECT
    #         a.name AS airline,
    #         IFNULL(SUM(at.flight_price), 0) AS revenue
    #     FROM
    #         `tabAirline` AS a
    #     LEFT JOIN
    #         `tabAirplane Ticket` AS at ON at.flight = a.name
    #     WHERE 1=1 {conditions}
    #     GROUP BY a.name
    # """, values=values, as_dict=True)


    columns = get_columns()
    data = get_data(filters)
    total_revenue = sum(d[1] for d in data)
    data_list = [list(row) for row in data]
    # total_row = ["Total", total_revenue]
    chart = get_chart(data_list, total_revenue)

    report_summary = [{
        "value": total_revenue,
        "indicator": "Green" if total_revenue > 0 else "Red",
        "label": "Total Revenue",
        "datatype": "Currency",
        "currency": ""
    }]
    
    return columns, data_list, total_revenue, chart, report_summary

def get_data(filters):
    airline_filter = filters.get("airline") if filters else None
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")

    # airline_filter = filters.get("airline") if filters else None
    # from_date = filters.get("from_date") or add_days(today(), -30)
    # to_date = filters.get("to_date") or today()

    conditions = ""
    values = []

    if airline_filter:
        conditions += "AND airline.name = %s\n"
        values.append(airline_filter)

    if from_date and to_date:
        conditions += "AND ticket.creation BETWEEN %s AND %s\n"
        values.extend([from_date, to_date])

    query = f"""
        SELECT
            COALESCE(airline.name, 'Other') AS airline,
            SUM(COALESCE(ticket.total_amount, 0)) AS revenue
        FROM
            tabAirline AS airline
        LEFT JOIN
            `tabAirplane Ticket` AS ticket
        ON
            airline.name = SUBSTRING_INDEX(ticket.flight, '-', 1)
        WHERE
            1=1
            {conditions}
        GROUP BY
            airline.name
        ORDER BY
            revenue DESC
    """

    data = frappe.db.sql(query, values)
    return data



def get_chart(data, total_revenue):
    chart = {
        "data": {
            "labels": [d[0] for d in data[:-1]],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d[1] for d in data[:-1]]
                }
            ]
        },
        "type": "donut",
        "center": {
            "text": "Total Revenue",
            "subtext": frappe.format_value(total_revenue, dict(fieldtype='Currency')),
            "style": {
                "fill": "green",
                "font-size": "14px",
                "font-weight": "bold"
            }
        }
    }

    return chart

