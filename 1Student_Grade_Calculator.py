'''
Topic: Student Grade Calculator
កម្រិត: Beginner
ពេលវេលា: 15-30 នាទី
Concept: Variables, Input, If / Elif / Else, Operators
'''
# Requirements
print("===== STUDENT GRADE CALCULATOR =====")
# Input ឈ្មោះសិស្ស
name = input("Enter your name :")

# Input ពិន្ទុចំនួន 3 មុខវិជ្ជា
pythonScore = float(input("Enter your python score :"))
databaseScore = float(input("Enter your data base score :"))
cppScore = float(input("Enter your C++ score :"))
print("====================================")

# បើពិន្ទុតិចជាង 0 ឬលើស 100 ត្រូវបង្ហាញ Invalid Score
# if all(score < 0 or score > 100 for score in [pythonScore, databaseScore, cppScore]):
    # print("Invalid Score")
if pythonScore < 0 or pythonScore > 100:
    print("Invalid Score")
elif databaseScore < 0 or databaseScore > 100:
    print("Invalid Score")
elif cppScore < 0 or cppScore > 100:
    print("Invalid Score")
else:
    # Calculate Total Score
    totalScore = pythonScore + databaseScore + cppScore

    # Calculate Average Score
    averageScore = totalScore / 3

    # កំណត់ Grade តាមពិន្ទុមធ្យម៖
    if averageScore >= 90:
        Grade = "A"
    elif averageScore >= 80:
        Grade = "B"
    elif averageScore >= 70:
        Grade = "C"
    elif averageScore >= 60:
        Grade = "D"
    elif averageScore >= 50:
        Grade = "E"
    else:
        Grade = "F"

    # បើ Average >= 50 បង្ហាញ Pass។
    if averageScore >= 50:
        Status = "Pass"
    # បើ Average < 50 បង្ហាញ Fail។
    elif averageScore < 50:
        Status = "Fail"

    # Display 
    print("\n\n===== Student Result =====")
    print(f"Name: {name}")
    print(f"Total Score: {totalScore:.2f}") # ប្រើ :.2f ដើម្បីបង្ហាញលេខទសភាគ 2 ខ្ទង់/
    print(f"Average: {averageScore:.2f}") # ប្រើ :.2f ដើម្បីបង្ហាញលេខទសភាគ 2 ខ្ទង់/
    print(f"Grade: {Grade}")
    print(f"Status: {Status}")
    print("==========================")
    
    