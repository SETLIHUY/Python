# Project: Daily Expense Tracker

print("===== DAILY EXPENSE TRACKER =====")
# 1.ទទួល Initial Balance ពី User។
balance = float(input("Enter your balance $: "))

# 11.បដិសេធការបញ្ចូលចំណាយអវិជ្ជមាន ឬស្មើសូន្យ
if balance <= 0 :
    print(f"Invalid balance: {balance}")
    exit()

# 2.សួរចំនួន Expense ដែលចង់បញ្ចូល។
numExpense = int(input("How many expense?: "))

# 12.បដិសេធការបញ្ចូល numExpense អវិជ្ជមាន ឬស្មើសូន្យ
if numExpense <= 0 :
    print(f"Invalid num Expense: {numExpense}")
    exit()            
    

# 3.ប្រើ list ដើម្បីរក្សាទុកចំណាយទាំងអស់។
expenses = []

# 4.ប្រើ for loop ដើម្បីទទួលចំណាយនីមួយៗ។
for i in range(1, numExpense + 1):
    amount = float(input(f"Expenses {i}: "))

    # 14.បដិសេធការបញ្ចូលចំណាយអវិជ្ជមាន ឬស្មើសូន្យ។
    if amount <= 0:
        print(f"Invalid amount {i}: {amount}")
        exit()
    expenses.append(amount)
print("=================================\n")            
        
    
# 5.គណនា Total Expense។
totalExpense = sum(expenses) 
# for i in range(0 , numExpense):
#     if i < numExpense:      
#         totalExpense = totalExpense + expenses[i]  
# print(totalExpense)          

# 13.គណនា Average Expense
averageExpense = totalExpense / len(expenses)

# 9.បើចំណាយលើស Balance បង្ហាញ Insufficient Balance។     
if balance < totalExpense:
    print(f"Insufficient Balance: ${balance:.2f} < total: ${totalExpense:.2f}")
    exit()

# 6.គណនា Remaining Balance។
remainingBalance = balance - totalExpense
# print(remainingBalance)

# 8.found good budget and bad budget
if balance - (balance * 1/2) >= totalExpense:
    status = "Good Budget"
else :
    status = "Bad Budget"

# 10.បង្ហាញចំណាយដែលមានតម្លៃខ្ពស់បំផុតដោយប្រើ max()។
#    បង្ហាញចំណាយដែលមានតម្លៃទាបបំផុតដោយប្រើ min()។
highestPrice = 0
lowestPrice = 0
highestNum = 1
lowestNum = 1

for i in range(0 , numExpense):
    if i == 0:
        highestPrice = expenses[0] 
        lowestPrice = expenses[0]
        highestNum = 1
        lowestNum = 1
    else :
        if highestPrice < expenses[i]:
            highestPrice = expenses[i]
            highestNum = i + 1
        if lowestPrice > expenses[i]:
            lowestPrice = expenses[i]
            lowestNum = i + 1

# highestPrice = max(expenses)
# lowestPrice = min(expenses)
# highestNum = expenses.index(highestPrice) + 1
# lowestNum = expenses.index(lowestPrice) + 1

# print(higthestPrice, higthestNum)
# print(lowestPrice, lowestNum)

# 7.បង្ហាញចំណាយទាំងអស់ និងប្រាក់ដែលនៅសល់។
print("===== EXPENSE REPORT =====")
print(f"Initial Balance: ${balance:.2f}\n")
print("Expense List:")
for i in range(0, numExpense):
    print(f"{i+1}. ${expenses[i]:.2f}")
print(" ") 
print(f"Total Expense: ${totalExpense:.2f}\n")
print(f"Remaining Balance: ${remainingBalance:.2f}\n")
print(f"Average Expense: ${averageExpense:.2f}\n")
print(f"higthestNum: {highestNum} = higthestPrice: ${highestPrice:.2f}\n")
print(f"lowestNum: {lowestNum} = lowestPrice: ${lowestPrice:.2f}\n")
print(f"Status: {status}!")
print("==========================")  