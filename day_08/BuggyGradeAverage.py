def BuggyGradeAverage(gradeSum , numberOfGrades): 
    if numberOfGrades == 0 :
        return 0
    average = int(gradeSum / numberOfGrades) 
    return average

counter= 0 
total =0 

while True :
    print((counter+1),"."," Enter the Grades or type 'done' to finish: " )
    grade = input()
    if grade == 'done' : 
        break
    counter += 1
    total += int(grade)
    


averageGrade = BuggyGradeAverage(total , counter)
print("The Average Grade is: ", averageGrade)