# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]
k = int(input('Введите сдвиг: '))
newList = []

for i in range(k % len(list)):
    newList.insert(0, list[- 1 - i])
for i in range(len(list) - k):
    newList.append(list[i])
print(newList)
