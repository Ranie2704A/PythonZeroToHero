# key : value -> key are immutable, values are not

family = {"Abad" : 22, "Abril": 0.7, "Sharon" : 25}
print(family)

#Or specific values
print(family["Abad"])

#Or with get, with an else value if the key doesn't exist
print(family.get("Peyer", "No existe"))

#Change the value of one key
family["Abad"] = 22.7
print(family)

#Add elements
family["Fernando"] = 25
print(family)

#Delete elements -> specific elements
del family["Fernando"]
print(family)

#Is in the dictionary?
print("Peyer" in family)