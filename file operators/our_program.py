
fr_all_students = open("file operators\\all_students.txt","r")
fr_passed_students = open("file operators\\passed_students.txt","r")

fr_all_students_list = [line.rstrip("\n")for line in fr_all_students]
fr_passed_students_list = [line.rstrip("\n")for line in fr_passed_students]

print("all students",fr_all_students_list)
print("passed students",fr_passed_students_list)

failed_students = set(fr_all_students_list).difference(fr_passed_students_list)
print("failed",failed_students)  
