# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = input('Введите числа через пробел: ')
my_list = [int(i) for i in list.split(' ')]

new_list = []
number = int(len(my_list))

for i in range(len(my_list)):
	while i < len(my_list)/2 and number > len(my_list)/2:
		number = number - 1
		a = my_list[i] * my_list[number]
		new_list.append(a)
		i += 1

print(my_list)
print(new_list)
