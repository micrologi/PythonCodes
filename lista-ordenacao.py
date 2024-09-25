my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
my_list_sort = my_list.copy()
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
print(my_list)
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
print(my_list_sort)
my_list_sort.sort()
print(my_list_sort)

my_list_reverse = my_list_sort.copy()
my_list_reverse.reverse()
print(my_list_reverse)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

new_list = my_list[1:4]
print(new_list)
