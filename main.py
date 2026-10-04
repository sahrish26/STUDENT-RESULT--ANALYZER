import result_analyzer


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if mark < 0 or mark > 100:
                print("Error: Marks must be between 0 and 100.")
            else:
                return mark

        except ValueError:
            print("Error: Please enter a valid number.")


def display_result(name, subjects, marks):
    total = result_analyzer.calculate_total(marks)
    average = result_analyzer.calculate_average(marks)

    maximum_marks = len(marks) * 100
    percentage = result_analyzer.calculate_percentage(
        marks, maximum_marks
    )

    grade = result_analyzer.calculate_grade(percentage)
    result = result_analyzer.calculate_result(marks)

    print("\n========== STUDENT RESULT ==========")
    print("Student Name:", name)

    print("\nSubject Marks:")

    for subject, mark in zip(subjects, marks):
        print(f"{subject}: {mark}")

    print("\nTotal Marks:", total)
    print("Average:", round(average, 2))
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)
    print("====================================")


def main():
    print("====================================")
    print("      STUDENT RESULT ANALYZER")
    print("====================================")

    name = input("Enter student name: ").strip()

    while name == "":
        print("Error: Student name cannot be empty.")
        name = input("Enter student name: ").strip()

    subjects = [
        "Python",
        "Digital Electronics",
        "Computer Networks",
        "Web Designing",
        "Database"
    ]

    marks = []

    for subject in subjects:
        mark = get_mark(subject)
        marks.append(mark)

    display_result(name, subjects, marks)


try:
    main()

except Exception as error:
    print("An unexpected error occurred:", error)
