list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию
m_max = 0
m_pos = 0
pos = len(list_numbers) - 1

for i in range(len(list_numbers)):
    if list_numbers[i] >= m_max:
        m_max = list_numbers[i]
        m_pos = i

a = list_numbers[pos]
list_numbers[pos] = list_numbers[m_pos]
list_numbers[m_pos] = a

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]