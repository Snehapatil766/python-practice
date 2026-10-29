students = ["Sneha", "Rahul", "Priya", "Amit"]

print("Total students:", len(students))

name = input("Search student: ")
if name.lower() in [s.lower() for s in students]:
    print("Student is present")
else:
    print("Student is absent")

new_student = input("Enter new student: ")
students.append(new_student)

absent_student = input("Enter absent student to remove: ")
for student in students:
    if student.lower() == absent_student.lower():
        students.remove(student)
        break

print("Updated list:", students)