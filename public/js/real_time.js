frappe.ready(function() {
    // Listen to the 'message_received' event
    // Listen to the 'message_received' event
frappe.realtime.on('message_received', (data) => {
    console.log('Received realtime event:', data);
    // Display the message in a notification or UI element
    frappe.msgprint({
        title: __('New Message'),
        message: __(data.content),
        indicator: 'green'
    });
});

// Optionally, you can trigger the event manually for testing
frappe.call({
    method: 'first_app.first_app.Custom.event_listener.trigger_event',
    callback: function(response) {
        console.log(response.message);
    }
})});
