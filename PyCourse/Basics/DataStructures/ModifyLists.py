
names = ["Abad", "Abril", "Sharon"]
ages = [22, 23, 25]
is_approved = [True, False, True]

#Modify elements (append ->add at end of the list)
#(insert -> add for index
#(remove -> delete via element)
#(clear -> delete the entire list)

names.insert(2,"Peter")
ages.append(33)
is_approved.append(False)

#How can I know the index of the element?
print("The index of Abad is:", names.index("Abad"))

print(names)
print(ages)
print(is_approved)

#How I know if the element is on the list?
print("Caesar" in names)

#Edit the elemets
names[0] = "Michael Abad"

names.remove("Peter")
print(names)
ages.clear()
print(ages)

ages.append(22)





