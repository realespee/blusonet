frappe.ui.form.on("Employee", {
    company : function(frm) {

        console.log(frm)
        let company = frm.doc.company

        if ((company == "BluSonet") || (company == "Blu-UnitedStates")) {
            // change fieldname from PAN Number to TIN
            frm.set_df_property("pan_number", "label", "TIN Number")
            frm.refresh()
        }
    },

    refresh(frm) {
        
        let company = frm.doc.company

        if ((company == "BluSonet") || (company == "Blu-UnitedStates")) {
            // change fieldname from PAN Number to TIN
            frm.set_df_property("pan_number", "label", "TIN Number")
        }
    }
});