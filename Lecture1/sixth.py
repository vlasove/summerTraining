names = ['Alice', 'Bob', 'Alice', 'Vlad', 'Bob', 'Alice']
set_names = set(names)
print(set_names)

ss = set(['Alice', 'Bob', 'FGSHAKJJH'])
result = set_names.intersection(ss)
union = set_names.union(ss)
print(result)
# print(result[1])


# list() ------ Массив, упорядоченный (индексируемый), изменяемый
# tuple() ----- Массив, упорядоченный (индексируемый), неизменяемый
# set() ----- Нечто, неупорядоченное , изменяемое, хранит уникальные значения


# Ассоциативный массив - неупорядоченный набор пар ключ:значение.


dict_ex = dict()
dict_ex2 = {}
dict_nums = {'one': [1, 2, 4], 'two': 2, 'three': 3, 10: 234, 1: 3432, False: 13243,
             None: 13421342234, 65.432: 647389, (2, 3): 43234}
print(dict_nums['one']+[dict_nums['two']])

dict_nums['four'] = 21344

print(dict_nums.keys())
print(dict_nums.values())
print(dict_nums.items())
