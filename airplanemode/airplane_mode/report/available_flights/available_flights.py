# Copyright (c) 2025, Shivani Sahu and contributors
# For license information, please see license.txt

# import frappe


import frappe

def get_conditions(filters):
    conditions = []

    if filters.get('from_date'):
        conditions.append(f"date_of_departure >= '{filters['from_date']}'")
    if filters.get('to_date'):
        conditions.append(f"date_of_departure <= '{filters['to_date']}'")
    if filters.get('airplane'):
        conditions.append(f"airplane = '{filters['airplane']}'")

    return " AND ".join(conditions)

def execute(filters=None):
    conditions = get_conditions(filters or {})
    if conditions:
        conditions = f"WHERE {conditions}"
    else:
        conditions = ""

    query = f"""
        SELECT
            name,
            airplane,
            date_of_departure,
            source_airport,
            destination_airport,
            status
        FROM
            `tabAirplane Flight`
        {conditions}
        ORDER BY
            date_of_departure ASC
    """
    data = frappe.db.sql(query, as_dict=True)

    # Optional: define columns explicitly if needed
    columns = [
        {"label": "Flight ID", "fieldname": "name", "fieldtype": "Link", "options": "Airplane Flight", "width": 140},
        {"label": "Airplane", "fieldname": "airplane", "fieldtype": "Link", "options": "Airplane", "width": 120},
        {"label": "Departure Date", "fieldname": "date_of_departure", "fieldtype": "Date", "width": 120},
        {"label": "Source", "fieldname": "source_airport", "fieldtype": "Data", "width": 100},
        {"label": "Destination", "fieldname": "destination_airport", "fieldtype": "Data", "width": 100},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]

    return columns, data



# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

# def get_conditions(filters):
#     conditions = []

#     if filters.get('from_date'):
#         conditions.append(f"flight_date >= '{filters['from_date']}'")
#     if filters.get('to_date'):
#         conditions.append(f"flight_date <= '{filters['to_date']}'")
#     if filters.get('airplane'):
#         conditions.append(f"airplane = '{filters['airplane']}'")

#     return " AND ".join(conditions)

# def execute(filters=None):
#     conditions = get_conditions(filters or {})
#     if conditions:
#         conditions = f"WHERE {conditions}"

#     query = f"""
#         SELECT
#             name,
#             airplane,
#             date_of_departure,
#             source_airport,
#             destination_airport,
#             status
#         FROM
#             `tabAirplane Flight`
#         {conditions}
#         ORDER BY
#             date_of_departure ASC
#     """
#     data = frappe.db.sql(query, as_dict=True)
#     return data


# def get_data(filters):
#     conditions = []
    
#     if filters.get('from_date'):
#         conditions.append(f"flight_date >= '{filters['from_date']}'")
        
#     if filters.get('to_date'):
#         conditions.append(f"flight_date <= '{filters['to_date']}'")
        
#     if filters.get('airplane'):
#         conditions.append(f"airplane = '{filters['airplane']}'")
    
#     where_clause = " AND ".join(conditions)
#     if where_clause:
#         where_clause = "WHERE " + where_clause
    
#     return frappe.db.sql(f"""
#         SELECT
#             name,
#             airplane,
#             flight_date,
#             source,
#             destination
#         FROM
#             `tabAirplane Flight`
#         {where_clause}
#         ORDER BY
#             flight_date ASC
#     """, as_dict=True)
