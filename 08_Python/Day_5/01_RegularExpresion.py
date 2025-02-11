import re
string = "Good morning all, good boy is intelligent,  good is always good and actually not ending it."
search = re.search("good", string, re.I)
match = re.match("good", string, re.I)
findall = re.findall("good", string, re.I)
# print(match)
# print(search)
# print(findall)
# if match:

match1 = re.findall("(?i)Morning", string)
# print(match1)

match2 = re.findall("good morning", string, re.I | re.DOTALL) #find find the string if present it show.
# print(match2)

match3 = re.search("good morning", string, re.I | re.DOTALL) #Search give the location
# print(match3)
myspan = match3.span() #it give starting and ending location.
# print(myspan)

l=[]
for i in re.finditer(re.escape("good"), string,re.I):
    # print(i)
    l.append(i.span())
#     print(i)

# print(l)

match4 = re.sub("(?i)good", "Nice",string) #(?i) is use for Ignorecase sensitivity.
# print(match4)
# print(string)

string1 = '''hi
enter 
how re you 
jevlis ka'''
match5 =re.split("\n",string1)
# print(match5)

pattern = r'[a].*' #starting from a and print upto last
match6 = re.findall(pattern,string)
#print(match6)

pattern = r'[a].?' #starting from a and print upto last
match7 = re.findall(pattern,string)
print(match7)