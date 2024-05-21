import frappe
# Function to delete Quiz documents with status = Submitted
submitted_quiz = frappe.get_list("Quiz", filters={"status": "Submitted"}, fields=["name"])
print(len(submitted_quiz))
@frappe.whitelist()
def delete_submitted_quiz():
    try:
        # Get list of Quiz documents with status = Submitted
        submitted_quiz = frappe.get_list("Quiz", filters={"status": "Submitted"}, fields=["name"])
        
        # Delete each submitted quiz document
        for question in submitted_quiz:
            frappe.delete_doc("Quiz", question["name"], ignore_permissions=True)
    except Exception as e:
        frappe.log_error("Error deleting submitted quizzes: {0}".format(str(e)))

# Enqueue the scheduler function
frappe.enqueue('first_app.schedular.backgroundjob.delete_submitted_quiz')
