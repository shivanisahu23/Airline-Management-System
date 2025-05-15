// Copyright (c) 2025, Shivani Sahu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Monthly Input", {
	refresh(frm) {
        frm.disable_save();
	},
    click_here:function(frm){
        frappe.call({
            method:"airplanemode.airplane_mode.doctype.monthly_input.monthly_input.get_value",
            args: {
                name1 :frm.doc.name1,
                amount: frm.doc.amount,
                fiscal_year: frm.doc.fiscal_year,
                month: frm.doc.month
            },


        })
        // console.log(frm.doc.amount)

        
    }
    
});

// let.log('child',child)
        // // frm.re child = frm.add_child('table', {
        //     name: frm.doc.name, 
        //     amount: frm.doc.amount
        // });
        // consolefresh_field('table')