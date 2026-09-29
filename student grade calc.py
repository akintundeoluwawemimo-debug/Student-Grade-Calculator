print("STUDENT GRADE CALCULATOR")
def get_score (subject):
    while True :
        score = int(input("Enter " + subject + " score :"))
        if 0 <= score <= 100 :
            return score 
        else :
            print("Invalid score !. Enter a score between 0 - 100")
   
name = input("Enter student's name: ")

print("Welcome," , name)

math = get_score("Mathematics")
eng = get_score("English")
bio = get_score("Biology")
phy = get_score("Physics")
chem = get_score("Chemistry")
 
total = math + eng + bio + phy + chem
average = total / 5

print("Total = ", total)
print("Average = ", average)

if average >= 70 : 
    grade = "A"
elif average >= 60 :
       grade = "B"
elif average >= 50 :
       grade = "C"
elif average >=40 :
       grade = "D"
else :
     grade = "F"
   
print("Grade:", grade)

if average >= 50 :
    status = "pass"
else :
      status = "fail"
print("Status:" , status)


print()
print("   FINAL RESULT   ")
print("Student Name :" , name)
print(" Total score :", total)
print(" Average score:", average)
print("Grade :", grade)
print("Status :", status)

if status == "fail" :
    print("Try to put more effort,", name , ",you can do it ")
else :
        print("You did well, " , name)