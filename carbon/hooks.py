# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "carbon"
app_title = "Erpnext Energy Scada Carbon Accounting"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Energy Scada Carbon Accounting for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/carbon/css/carbon.bundle.css"
app_include_js = "/assets/carbon/js/carbon.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "carbon.engine.on_document_submit",
        "on_cancel": "carbon.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "carbon.engine.daily_scheduled_sync"
    ]
}
