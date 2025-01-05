#Tuples are not mutable, but they're faster than lists

clients_names = ("Abad", "Sharon", "Abril")
clients_ages = (22,25,21)
is_super_client = (True, False, True)

abad_age = clients_ages[0]

print(clients_names)
print(clients_ages)

print(abad_age)

#Fx length

print(len(clients_names))

#Fx index

print(clients_names.index("Sharon"))

#Fx count

print(clients_names.count("Abril"))

