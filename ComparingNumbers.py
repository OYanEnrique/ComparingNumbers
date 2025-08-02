#Comparing  Numbers

first_number=int(input('Enter a number:\n'))
second_number=int(input('Enter another number:\n'))

if first_number > second_number:
	print(f'The number {first_number} is greater than the number {second_number}')
elif first_number == second_number:
	print(f'The number {first_number} is equal to the number {second_number}')
else:
	print(f'The number {second_number} is greater than the number {first_number}')
	