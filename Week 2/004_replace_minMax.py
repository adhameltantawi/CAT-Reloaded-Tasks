n = int(input())
my_list = list(map(int,(input().split())))
listMin = my_list.index(min(my_list))
listMax = my_list.index(max(my_list))
my_list[listMin], my_list[listMax] = my_list[listMax], my_list[listMin]
print (*my_list)