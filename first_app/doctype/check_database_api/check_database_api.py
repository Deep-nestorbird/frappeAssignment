# Copyright (c) 2024, Deep Prakash Srivastava and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class check_database_api(Document):
# 	pass
# In your custom Python file (e.g., myapp/api/employee_api.py)
import frappe
from frappe import _

# Define a new API endpoint to fetch the list of employees
@frappe.whitelist(allow_guest=True)
def get_employee_list():
    # Use frappe.get_list to fetch the list of Employees
    employees = frappe.get_list('Employee')
    return employees


@frappe.whitelist(allow_guest=True)
def get_employee_list1():
    # Use frappe.get_list to fetch the list of Employees
    employees = frappe.get_list('Employee')

    # Return the list of employees
    return employees


@frappe.whitelist(allow_guest=True)
def get_employee_list3():
    # Use frappe.get_list to fetch the list of Employees
    employees = frappe.db.get_list('Employee',
    filters={
        'designation': 'abcd'
    })

    # Return the list of employees
    return employees


@frappe.whitelist(allow_guest=True)
def get_employee_list2():
    # Use frappe.get_list to fetch the list of Employees
    employees = frappe.get_all('Employee')

    # Return the list of employees
    return employees