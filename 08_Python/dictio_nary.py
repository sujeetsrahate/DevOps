person = {"FirstName": "Sujeet", 
        "lastName":"Rahate",
          "Skills":["python", "Java", "SQL", "DBMS"],
            "skills":{
    "backend_skills":["nohejs", "ruby"],
    "database":["redis","sql", "java"]
}}
# print(len(person))
# print(person["skills"]["backend_skills"])

# print(person.get("FirstName"))
# print("lastName" in person)
# print(person.pop("FirstName"))
# print(len(person))
# del person["lastName"]
# print(len(person))
# print(person.get("skills"))
# person["skills"]["database"].append("mongodb")
# print(person["skills"]["database"])


print(person.items())
person_copy = person.copy()
del person
# print(person_copy)
# print(person_copy.keys()  #printing the key values
keys=person_copy.keys()
for i in keys:
    print(person_copy[i])