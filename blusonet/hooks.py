from . import __version__ as app_version

app_name = "blusonet"
app_title = "BluSonet"
app_publisher = "Simon"
app_description = "BluSonet"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "wanyamasp@gmail.com"
app_license = "MIT"


# FIXTURES
fixtures = [
	"Custom Field"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/blusonet/css/blusonet.css"
# app_include_js = "/assets/blusonet/js/blusonet.js"

# include js, css files in header of web template
# web_include_css = "/assets/blusonet/css/blusonet.css"
# web_include_js = "/assets/blusonet/js/blusonet.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "blusonet/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Employee" : "public/js/employee.js",
	 "Sales Invoice" : "custom_script/sales_invoice/sales_invoice.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "blusonet.install.before_install"
# after_install = "blusonet.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "blusonet.uninstall.before_uninstall"
# after_uninstall = "blusonet.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "blusonet.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo"
	'Sales Invoice': 'blusonet.custom_script.overrides.sales_invoice.custom_sales_invoice.CustomSalesInvoice'
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"blusonet.tasks.all"
# 	],
# 	"daily": [
# 		"blusonet.tasks.daily"
# 	],
# 	"hourly": [
# 		"blusonet.tasks.hourly"
# 	],
# 	"weekly": [
# 		"blusonet.tasks.weekly"
# 	]
# 	"monthly": [
# 		"blusonet.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "blusonet.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "blusonet.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "blusonet.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"blusonet.auth.validate"
# ]

