def get_number_input(msj: str, err: str = 'Error: Must be a number') -> int:
    while True:
        try:
            return int(input(msj))
        except ValueError:
            print(err)
            continue

def get_students_names(qty: int) -> list:
    students_list = []
    for i in range(qty):
        student = input(f"Enter student name: ({i+1} of {qty})")
        students_list.append(student)
    return students_list

def create_student_grades(number_of_subjects: int) -> dict[str, int]:
    grades = {}

    for i in range(number_of_subjects):
        subject = input(f"Enter subject name: ({i+1} of {number_of_subjects})")
        message = f"Enter subject grade: ({i+1} of {number_of_subjects})"
        while True:
            grade = get_number_input(message)
            if grade > 100 or grade < 0:
                print('Grade must be between 0 and 100')
                continue
            break
        grades[subject] = grade

    return grades

def calculate_avg_grade(grades: dict[str, int]) -> float:
    if not grades:
        return 0.0  # Prevent division by zero
    return sum(grades.values()) / len(grades)

def group_grades_by_subject(data: dict[str, dict]) -> dict[str, dict]:
    grades_by_subject = {}
    for student, grades in data.items():
        for subject, grade in grades.items():
            if subject not in grades_by_subject:
                grades_by_subject[subject] = {}
            grades_by_subject[subject][student] = grade
    return grades_by_subject

def max_grade_subject(data: dict[str, dict]) -> dict[str, dict]:
    return {
        subject: {max_student[0]: max_student[1]}
        for subject, max_student in (
            (subject, max(students.items(), key=lambda x: x[1])) for subject, students in data.items()
        )
    }

def failing_students(data: dict[str, dict]) -> set[str]:
    failing_students = set()
    for student, subjects in data.items():
        if any(grade < 60 for grade in subjects.values()):
            failing_students.add(student)
    return failing_students

if __name__ == "__main__":
    data = {}
    students_qty = get_number_input('Enter number of students: ')
    students_names = get_students_names(students_qty)

    for student in students_names:
        qty_subjects = get_number_input(f'How many subjects for {student}?: ')
        data[student] = create_student_grades(qty_subjects)

    averages = []

    for student, grades in data.items():
        avg_grade = calculate_avg_grade(grades)
        print(f'Student {student} has average grade: {avg_grade}')
        averages.append(avg_grade)

    grades_by_subject = group_grades_by_subject(data)

    highest_score_subject = max_grade_subject(grades_by_subject)
    print('Highest score by subject:', highest_score_subject)

    class_avg = sum(averages) / len(averages) if averages else 0
    print(f'Class average: {class_avg}')

    print('The following students failed:')
    for student in failing_students(data):
        print(student)
