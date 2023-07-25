#! usr/bin/python3

executive_names = ("Precious", "Gift", "Goodness", "Precious")
edited = list(executive_names)
edited.insert(4,"Favour")
edited.insert(5,"Victor")
edited.insert(6, "Praise")
executive_names = tuple(edited)
edited = list(executive_names)

executive_names = tuple(edited)

#Tuples does not allow manipulation of initila list
#print(executive_names)
if "Victor" in executive_names:
    print("Present!")
else:
    print("Absent!")