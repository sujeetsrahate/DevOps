import os
print("Current Directory", os.getcwd())
try:
    f = open(f"C:\\Users\\Administrator\\devops\\08_Python\\Day_5\\file1.txt")
    # print(f.read())
    # print(f.readline()) #single line show
    # print(type(f.readline())) #String
    # print(type(f.readlines()))#list
    # print(f.readlines()) # show all the lines
    
finally:
    f.close()
os.remove(f"C:\\Users\\Administrator\\devops\\08_Python\\Day_5\\file1.txt")
print
