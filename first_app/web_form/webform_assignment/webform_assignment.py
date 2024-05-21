import frappe

def get_context(context):
	pass
@frappe.whitelist(allow_guest=True)
def send_form_submission_notification(email):
    try:
        # Trigger email notification
        frappe.sendmail(
            recipients=email,  # Set the recipient email address
            subject='Form Submission Notification',  # Set the email subject
            content='Welcome to Erpnext',  # Set the email content
            now=True  # Send the email immediately
        )

        return "Form submitted successfully"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Form Submission Error")
        return "An error occurred while submitting the form"