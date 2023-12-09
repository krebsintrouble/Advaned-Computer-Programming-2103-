english_grade = float(input("Enter English grade: "))
filipino_grade = float(input("Enter Filipino grade: "))
science_grade = float(input("Enter Science grade: "))
math_grade = float(input("Enter Math grade: "))
araling_panlipunan_grade = float(input("Enter Araling Panlipunan grade: "))
physical_grade = float(input("Enter Physical Education grade: "))


total_grades = (english_grade + filipino_grade + science_grade + math_grade + araling_panlipunan_grade + physical_grade)
average_grade = total_grades / 6

print("Your average grade is:", average_grade)
