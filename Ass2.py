def check_attendance(login_time):
    if login_time < 9.30:
        return "Present"
    elif 9.30 <= login_time <= 10.00:
        return "Late"
    else:
        return "Absent"
print(check_attendance(9.15))  