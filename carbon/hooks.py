# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "carbon"
app_title = "Erpnext Energy Scada Carbon Accounting"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Energy Scada Carbon Accounting - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/carbon/css/carbon.bundle.css"
app_include_js = "/assets/carbon/js/carbon.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Energy Scada Carbon Accounting Entry": {
        "validate": "carbon.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "carbon.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "carbon.tasks.hourly_sync"
    ],
    "daily": [
        "carbon.tasks.daily_reconciliation"
    ],
    "weekly": [
        "carbon.tasks.weekly_digest"
    ]
}
