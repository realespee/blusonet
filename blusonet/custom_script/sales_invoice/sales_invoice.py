# import frappe
# import json

# @frappe.whitelist()
# def map_coupon(coupon):
#     coupon_json = json.loads(coupon)
#     print('\n\n COUPON JSON\n', coupon_json, '\n\n')
#     print('\n\n COUPON JSON\n', coupon_json[0]['coupon_code'], '\n\n')
#     coupon = coupon_json[0]['coupon_code']
#     pos_coupon = frappe.get_doc("POS Coupon", coupon)
#     sales_person = pos_coupon.custom_sales_person
#     commission_rate = pos_coupon.custom_commission_rate

#     return {
#             'sales_person': sales_person,
#             'commission_rate': commission_rate
#         }