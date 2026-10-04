def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_percentage(marks, maximum_marks):
    total = calculate_total(marks)
    return (total / maximum_marks) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    for mark in marks:
        if mark < 35:
            return "FAIL"

    return "PASS"
