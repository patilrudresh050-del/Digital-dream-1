def check_intern_eligibility(age, percentage):
    if age >= 18 and percentage >= 60:
        return "Eligible: Age is 18 or above and percentage is 60 or above."
    else:
        return "Not Eligible: Age must be at least 18 and percentage must be at least 60."
print(check_intern_eligibility(20,65))