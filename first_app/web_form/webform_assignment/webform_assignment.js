frappe.ready(function() {
    // Bind events here
    // Example: Call the send_form_submission_notification function
    frappe.web_form.events.on("after_save", function() {
        var emailField = frappe.web_form.get_values().email; // Assuming "email" is the fieldname for the email address field
        if (emailField) {
            sendFormSubmissionNotification(emailField);
        }
    });
});

// Define the function to send form submission notification
function sendFormSubmissionNotification(email) {
    frappe.call({
        method: 'first_app.first_app.web_form.webform_assignment.webform_assignment.send_form_submission_notification', // Replace 'path.to' with the actual path to your Python function
        args: {
            email: email // Pass the email address as an argument
        },
        callback: function(response) {
            // Handle the response
            if (response.message) {
                console.log('Form submitted successfully');
            } else {
                console.error('Failed to submit form:', response.error);
            }
        }
    });
}