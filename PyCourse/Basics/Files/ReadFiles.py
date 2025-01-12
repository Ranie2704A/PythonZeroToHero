#Always close the files
#If the file isn't in the project, put the full directory
file = open("myfile.txt", "r")

print(file.readable()) #Verify if we can open the file

#Return all the content of the file:
# print(file.read())

#Return each line, one by one
# print(file.readline())
# print(file.readline())
# print(file.readline())

#Return all the content in an Array
# print(file.readlines()) #We can especify the index


#Read by loop
for line in file:
    print(line)

file.close()