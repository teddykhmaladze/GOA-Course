number_list = [45,46,47,48,49,50]
print(len(number_list)*2)


name_list = ["gio" , "andira" , "gurami" , "teodore"]
for i in range(len(name_list)):
    if i % 2 == 0:
        print(name_list[i])


data_list = [3.14, "Theodore", 5, False, "Luka"]
str_list = []
for x in range(len(data_list)):
    if type(data_list[x]) == str:
        str_list.append(data_list[x])
data_list += str_list 
print(data_list)


list1 = ["gio", "andira", "gurami", "teodore", "luka"]
list2 = []
for w in range(len(list1)):
    list2.append(list1[w].upper())
print(list2)