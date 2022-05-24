frappe.ui.form.on("Employee", {
    on_load(frm) {

        console.log(frm)

        if (frm.doc.company == "BluSonet") {
            frm.pan_number.label = "TIN"
        }
        else if(frm.doc.company == "Blu-UnitedStates") {
            frm.pan_number.label = "TIN Number"
        }
        else{
            frm.pan_number.label = "PAN Number"
        }
    }
});