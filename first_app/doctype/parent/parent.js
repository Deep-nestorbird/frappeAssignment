frappe.ui.form.on('Parent', {
    refresh: function(frm) {
        frm.add_custom_button(__('Add Child Row'), function() {
            openChildTableDialog(frm);
        });
    }
});

function openChildTableDialog(frm) {
    const childTableFields = [
        {"fieldname": "email", "fieldtype": "Data", "label": "Email"},
        {"fieldname": "dob", "fieldtype": "Date", "label": "Date of Birth"},
    ];

    const dialog = new frappe.ui.Dialog({
        title: __('Add Child Row'),
        fields: childTableFields,
        primary_action: function() {
            const values = dialog.get_values();
            if (values) {
                addDataToChildTable(frm, values);
                dialog.hide();
                frm.reload_doc();
            }
        }
    });
    dialog.show();
}

function addDataToChildTable(frm, data) {
    const childTable = frm.doc.details || [];
    const childRow = {};
    
    // Set values for the new row
    for (const key in data) {
        if (data.hasOwnProperty(key)) {
            childRow[key] = data[key];
        }
    }

    // Append the new row to the child table
    childTable.push(childRow);
    frm.refresh_field('details');
}
