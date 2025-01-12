#Sets doesn't have a specified order and are immutable

list_of_names = {"Abad", "Sharon", "Abril"}
print(list_of_names)

list_of_ages = {23,24,25}
print(list_of_ages)

#Fx add

list_of_names.add("Peter")
print(list_of_names)


#Fx length

print(len(list_of_names))

#Fx update -> like extends of a lists

list_of_ages.update(list_of_names)
print(list_of_ages)

#Fx remove and discard -> discard works finding coincidences so, if the element is not in the set, won't return an error
list_of_names.remove("Peter")
print(list_of_names)

#Fx pop -> delete an element randomly

list_of_names.pop()
print(list_of_names)
