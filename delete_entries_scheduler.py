import frappe
from frappe.utils.background_jobs import enqueue

def delete_entries():
    # Query entries to be deleted
    entries_to_delete = frappe.get_list("quiz", filters={}, limit_page_length=10)
    
    # Delete entries
    for entry in entries_to_delete:
        frappe.delete_doc("quiz", entry.name, ignore_permissions=True)

# Schedule the job to run every 2 minutes
def schedule_job():
    enqueue(
        method=delete_entries,
        queue='long',
        interval=120,  # Interval in seconds (2 minutes)
        now=True  # Execute the job immediately on app startup
    )
