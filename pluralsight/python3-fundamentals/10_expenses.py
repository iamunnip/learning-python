# expenses = [10.50, 8, 5, 15, 20, 5, 3]

# sum = 0

# for expense in expenses:
#   sum = sum + expense
  
# print("You spent $", sum, sep='')

# total = sum(expenses)

# print("You spent $", total, sep='')


total = 0
expenses = []
number_of_expenses = int(input("Enter the number of expenses "))

for i in range(number_of_expenses):
  expenses.append(float(input("Enter your expense ")))
  
total = sum(expenses)

print("You spent $", total, sep='')
