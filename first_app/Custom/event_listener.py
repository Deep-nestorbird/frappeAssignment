import frappe

@frappe.whitelist()
def trigger_event():
    message = {
        "content": "Hello, this is a realtime message!",
        "timestamp": frappe.utils.now()
    }
    # Trigger the event
    frappe.publish_realtime(event='message_received', message=message, user=frappe.session.user)
    return "Event triggered successfully"