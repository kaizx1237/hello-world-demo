subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)
gradeBook = list(zip(subjects, grades))

gradeBook.append(("visual arts", 83))
print(gradeBook)

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

full_gradebook = zip(gradeBook, last_semester_gradebook)