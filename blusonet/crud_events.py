import frappe


def before_submit(doc, method=None):
    # if doc.is_pos:
    #     pos_coupon = frappe.get_doc("POS Coupon", doc.posa_coupons[0].coupon)
         
    #     sales_partner = pos_coupon.custom_sales_partner
    #     commission_rate = pos_coupon.custom_commission_rate

    #     doc.sales_partner = sales_partner
    #     doc.commission_rate = commission_rate

    #     print('\n\n COUPON JSON\n Sales Partner: ', doc.sales_partner, '\t Commission Rate: ', doc.docstatus,'\n\n')


    #     doc.save()
    pass
