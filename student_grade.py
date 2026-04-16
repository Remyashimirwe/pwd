students=[]
sum = 0
average = 0
scores = []
numberStudents= int(input("please enter the number of the students: "))
for i in range(numberStudents):
    studentName= input("Enter the Student name: ")
    studentScore= int(input("Enter the Student Score: "))
    studDetail = {
    "name": studentName,
    "score": studentScore
    }
    students.append(studDetail)
for student in students:
    sum += student["score"]
average = sum/ len(students)
print(f"the average is {average}")
for student in students:
    scores.append(student["score"])
print(scores)
highest = max(scores)
lowest = min(scores)
for student in students:
    if student["score"] == highest:
        print(f"the top student is {student["name"]} with score of {student["score"]} ")
    if student["score"] == lowest:
        print(f"the lowest student is {student["name"]} with score of {student["score"]} ")

