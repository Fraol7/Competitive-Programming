def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        elif grade % 5 > 2:
            grade = (int(grade/5)+1)*5
            rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades
