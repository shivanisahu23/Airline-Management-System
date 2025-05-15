# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

import frappe

def get_conditions(filters):
    conditions = []

    if filters.get('from_date'):
        conditions.append(f"at.departure_date >= '{filters['from_date']}'")

    if filters.get('to_date'):
        conditions.append(f"at.departure_date <= '{filters['to_date']}'")

    if filters.get('airline'):
        conditions.append(f"af.airline = '{filters['airline']}'")

    return " AND ".join(conditions)


def execute(filters=None):
    filters = filters or {}
    conditions = get_conditions(filters)
    if conditions:
        conditions = "WHERE " + conditions

    query = f"""
        SELECT
            af.airline AS airline,
            at.name AS ticket_id,
            at.passenger,
            at.status,
            at.seat,
            at.flight_price,
            at.total_amount,
            at.departure_date
        FROM
            `tabAirplane Ticket` at
        JOIN
            `tabAirplane Flight` af ON at.flight = af.name
        {conditions}
        ORDER BY
            af.airline ASC, at.departure_date ASC
    """

    data = frappe.db.sql(query, as_dict=True)

    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline"},
        {"label": "Ticket ID", "fieldname": "ticket_id", "fieldtype": "Link", "options": "Airplane Ticket"},
        {"label": "Passenger", "fieldname": "passenger", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Seat", "fieldname": "seat", "fieldtype": "Data"},
        {"label": "Flight Price", "fieldname": "flight_price", "fieldtype": "Currency"},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency"},
        {"label": "Departure Date", "fieldname": "departure_date", "fieldtype": "Date"},
    ]

    return columns, data


# import frappe

# import frappe

# def get_conditions(filters):
#     conditions = []

#     if filters.get('from_date'):
#         conditions.append(f"departure_date >= '{filters['from_date']}'")

#     if filters.get('to_date'):
#         conditions.append(f"departure_date <= '{filters['to_date']}'")

#     if filters.get('airplane'):  # assuming the field is 'airplane' not 'airline'
#         conditions.append(f"airplane = '{filters['airplane']}'")

#     return " AND ".join(conditions)


# def execute(filters=None):
#     filters = filters or {}
#     conditions = get_conditions(filters)

#     if conditions:
#         conditions = f"WHERE {conditions}"

#     query = f"""
#         SELECT
#             name,
#             passenger,
#             status,
#             seat,
#             flight_price,
#             total_amount,
#             departure_date,
#             flight
#         FROM
#             `tabAirplane Ticket`
#         {conditions}
#         ORDER BY
#             departure_date ASC
#     """

#     data = frappe.db.sql(query, as_dict=True)

#     columns = [
#         {"label": "Ticket ID", "fieldname": "name", "fieldtype": "Link", "options": "Airplane Ticket"},
#         {"label": "Passenger", "fieldname": "passenger", "fieldtype": "Data"},
#         {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
#         {"label": "Seat", "fieldname": "seat", "fieldtype": "Data"},
#         {"label": "Flight Price", "fieldname": "flight_price", "fieldtype": "Currency"},
#         {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency"},
#         {"label": "Departure Date", "fieldname": "departure_date", "fieldtype": "Date"},
#         {"label": "flight", "fieldname": "flight", "fieldtype": "Link", "options": "Airplane Flight"},
#     ]

#     return columns, data


# def get_conditions(filters):
#     conditions = []

#     if filters.get('from_date'):
#         conditions.append(f"date_of_departure >= '{filters['from_date']}'")
    
#     if filters.get('to_date'):
#         conditions.append(f"date_of_departure <= '{filters['to_date']}'")
    
#     if filters.get('airline'): 
#         conditions.append(f"airplane = '{filters['airline']}'")

#     return " AND ".join(conditions)

    
# def execute(filters=None):
#     conditions = get_conditions(filters or {})
#     if conditions:
#         conditions = f"WHERE {conditions}"
#     else:
#         conditions = ""
    
# 	query = f"""
# 		SELECT
# 			name,
#             passenger,
#             status,
#             seat,
#             flight_price,
#             total_amount,
#             departure_date
#         FROM
# 			`tabAirplane Ticket`
#         {conditions}
# 		ORDER BY
# 			date_of_departure ASC
# 	"""
# 	data = frappe.db.sql(query, as_dict=True)

# 	columns = [
#         {"label": "Ticket ID", "fieldname": "name", "fieldtype":}
# 	]
	# columns, data = [], []
	# return columns, data


import frappe
from frappe.utils import today

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
    
    columns = get_columns()
    data = get_data(filters)
    total_revenue = sum(d[1] or 0 for d in data)
    data_list = [list(row) for row in data]
    total_row = ["Total", total_revenue]
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

    if airline_filter:
        data = frappe.db.sql("""
            SELECT
                al.name AS airline,
                SUM(at.total_amount) AS revenue
            FROM
                tabAirline AS al
            LEFT JOIN
                tabAirplane AS ai ON ai.airline = al.name
            LEFT JOIN
                tabAirplane Flight AS af ON af.airplane = ai.name
            LEFT JOIN
                tabAirplane Ticket AS at ON at.flight = af.name
            WHERE
                al.name = %s AND
                at.creation BETWEEN %s AND %s
            GROUP BY
                al.name
            ORDER BY
                revenue DESC
        """, (airline_filter, from_date, to_date))       #used it to pass a tuple value in %s to filter out airline 
    else:
        data = frappe.db.sql("""
            SELECT
                al.name AS airline,
                SUM(at.total_amount) AS revenue
            FROM
                tabAirline AS al
            LEFT JOIN
                tabAirplane AS ai ON ai.airline = al.name
            LEFT JOIN
                tabAirplane Flight AS af ON af.airplane = ai.name
            LEFT JOIN
                tabAirplane Ticket AS at ON at.flight = af.name
            WHERE
                at.creation BETWEEN %s AND %s
            GROUP BY
                al.name
            ORDER BY
                revenue DESC
        """, (from_date, to_date))
    
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