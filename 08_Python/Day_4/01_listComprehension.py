lang = "Python"
lst = list(lang)

# print(type(lst))
# print(lst)

lst1 = [i for i in lang]
# print(lst1)
# print(type(lst1))

lst2 = [i for i in range(20)]
# print(lst2)


lst3= [i * i for i in range(20)]
# print(lst3)

lst4 = [(i, i*i) for i in range(20)]
# print(lst4)
# print(type(lst4))
# print(lst4[2][1])

lst5 = [(i*2) for i in range(20)]
# print(lst5)

lst6 = [(i*2+1) for i in range(20)]
# print(lst6)

lst6 = [ i for i in range(20) if i>3 and i%2==0]
# print(lst6)

lst7 = [[1,2,3],[5,6,7],[23,46,66]] #it do list of list into single list
flat_list=[number for row in lst7 for number in row]
print(flat_list)




