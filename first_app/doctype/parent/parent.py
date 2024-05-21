# import frappe
# from frappe.model.document import Document

# class Parent(Document):
#     def submit_child_table_data(self, parent, details, data):
#         try:
#             # Get the child table
#             child_table = self.get(details)

#             # Append a new row to the child table
#             child_row = child_table.append('child_tables', {})

#             # Set values for the new row
#             for fieldname, value in data.items():
#                 child_row.set(fieldname, value)

#             # Save the parent document to persist changes
#             self.save()

#             return {"message": "Data submitted successfully"}
#         except Exception as e:
#             frappe.log_error(frappe.get_traceback(), "Error submitting data to child table")
#             return {"error": str(e)}
