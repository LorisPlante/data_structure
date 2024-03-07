def filter_students(students):
    return {name: avg for name, avg in students.items() if avg >= 15}
