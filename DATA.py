
from datetime import datetime as dt
dynamicMonth = dt.today()

PAYMENT = {
    "Mortgage": {
        "2022_RecurringMaintenance": [dynamicMonth, 299.00,  (f"Monthly Maintenance {dynamicMonth}")],
        "2022_RecurringPropertyTax": [dynamicMonth, 270.00,  (f"Monthly Property Tax {dynamicMonth}")],
        "2022_RecurringInsurance": [dynamicMonth, 270.00,  (f"Monthly Insurance {dynamicMonth}")],
        "2022_TenantRent": [dynamicMonth, 2600.00,  (f"Monthly Tenant Rent {dynamicMonth}")],
        "2022_MortgageDifference": [dynamicMonth, 1200.00,  (f"Monthly Mortgage Loss {dynamicMonth}")],
        "2022_Mortgage": [dynamicMonth, 3860.57,  (f"Monthly Mortgage Loss {dynamicMonth}")],
    },
    "Personal": {
        "2022_Rent": [dynamicMonth, 1200.00,  (f"Monthly Rent {dynamicMonth}")],
        "2022_Mortgage_Investment": [dynamicMonth, 1200.00,  (f"Monthly Rent {dynamicMonth}")],
        "2022_Cell_Phone": [dynamicMonth, 170.00,  (f"Monthly Cell Phone {dynamicMonth}")],
        "2022_Gym": [dynamicMonth, 70.00,  (f"Monthly Cell Phone {dynamicMonth}")]
    },
}

INCOME = {
    "Salary": {
        "2022_Monthly_Salary": [dynamicMonth,4000,(f"Monthly Salary {dynamicMonth}")],
        "2022_BiWeekly_Salary": [dynamicMonth,2000,(f"Monthly  {dynamicMonth}")]

    },
    "Variable": {
        "2022_BiWeeklyAverage": [dynamicMonth,300,(f"Monthly Cell Phone {dynamicMonth}")],
        "2022_MonthlyAverage": [dynamicMonth,900,(f"Monthly Cell Phone {dynamicMonth}")],
    },
    "Internship Hourly": {
        "2022_BiWeeklyAverage": [dynamicMonth,100,(f"Monthly Cell Phone {dynamicMonth}")],
        "2022_MonthlyAverage": [dynamicMonth,400,(f"Monthly Cell Phone {dynamicMonth}")],
    },
}