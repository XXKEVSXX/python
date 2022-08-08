#Calculating the average
quiz1 = float (input("Quiz#1: "))
quiz2 = float (input("Quiz#2: "))

if quiz1 >= 50 and quiz1 <= 100 and quiz2 >=50 and quiz2 <=100:
 
    Quiz_ave = (quiz1 + quiz2) /2
 
    

else:
    print("Invalid Value")

#Calculating the activities
activity1 = float(input("Activity#1: "))
activity2 = float(input("Activity#2: "))

if activity1 >= 50 and activity1 <= 100 and activity2 >=50 and activity2<=100:
    
    Activity_ave = (activity1 + activity2) /2
  
    

else:
    print("Invalid Value")

Exam_score = float (input("ExamScore: "))

if Exam_score >=1 and Exam_score <=50:
    
    Exam_ave = Exam_score + 50
 
else:
    print("Invalid Value")

print(" ")
print(" ")


print("Calculated Quiz: ", Quiz_ave)
print("Calculated Activities: ", Activity_ave )
print("Calculated Exam: ",Exam_ave)

Subject_grade_ave = (Quiz_ave +  Activity_ave +  Exam_ave  )/ 3

print("Subject Grade: ",Subject_grade_ave)

    



