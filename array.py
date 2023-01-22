##################----------problem 1 --------------################
expenses = [2200, 2350, 2600, 2130, 2190]
#In Feb, how many dollars you spent extra compare to January?S
print(f"expended extra in fabruary = {expenses[1] - expenses[0]}")
#2. Find out your total expense in first quarter (first three months) of the year.
print(f"total expenses in first quarter = {expenses[0] + expenses[1] + expenses[2]}")
#3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in expenses) # False
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expenses[3] = expenses[3] - 200
print(expenses)

##################----------problem 2 --------------################

heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print('Length of the list heros', len(heros))
#2. Add 'black panther' at the end of this list
heros.append('black panther')
#3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
#4. Now you don't like thor and hulk because they get angry easily :)So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print(heros.sort())

##################----------problem 3 --------------################
#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_num = int(input('enter max number: '))
odd_numbers = []
for i in range(1, max_num):
    if i % 2 != 0:
        odd_numbers.append(i)
print('Odd Numbers',odd_numbers)
