name_list = ["Abad", "Sharon", "Abril"]
ages_list = [25, 26, 27, 25]
approved_list = [True, False, True]
ages_list2 = [25, 26, 27, 25, 19]
names_copy = name_list.copy() #Fx copy

#Fx count -> returns the qty of times that an element appears
print(ages_list.count(25))

#Fx extends -> Join the elements
ages_list.extend(ages_list2)
print(ages_list)

#Fx pop -> delete and return an element (the last if an index is not provided)
ages_list.pop(2)
print(ages_list)

#Fx reverse -> make a reverse of the elements
name_list.reverse()
print(name_list)

#Fx sort -> Alph of numeric order
name_list.sort()
print(name_list)

print(names_copy)

