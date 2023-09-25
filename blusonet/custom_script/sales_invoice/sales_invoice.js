// frappe.ui.form.on("Sales Invoice", {
//     refresh: function(frm){
//         if(frm.doc.posa_coupons){
//             console.log('working POSA COUPON!!!!!!')
//             frm.set_value("sales_partner", 'Influencer 1')
//         }
//         console.log("After POSA COUPON!!!!!!!!!!");
//     },

//     posa_coupons: function(frm){
//         if(frm.doc.posa_coupons){
//             console.log('working POSA COUPON!!!!!!')
//             frm.set_value("sales_partner", 'Influencer 1')
//         }
//         console.log("After POSA COUPON!!!!!!!!!!");
//     },  
    
//     before_submit: function(frm) {
//         if(frm.doc.is_pos){
//             console.log("It is working")
//             console.log(frm.doc.posa_coupons)
//             frappe.call({
//                 method: "blusonet.custom_script.sales_invoice.sales_invoice.map_coupon",
//                 args: {
//                     'coupon': frm.doc.posa_coupons
//                 },
//                 callback: (res) => {
//                     console.log(res.message)
//                     frm.set_value("sales_partner", res.message.sales_partner)
//                 }
//             })
//         }
//     },
    
// })

