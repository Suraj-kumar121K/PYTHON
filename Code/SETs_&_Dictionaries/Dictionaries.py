dict = {
    "First Name":"Suraj",
    "Last Name":"Kumar",
    "Age": 22,
    "Gender":"Male"
}
# print(dict)

student = {
    "Name":"Suraj Kumar",
    "Subject" : {
        "Phy":45,
        "Chem":29,
        "Math":63
    }
}
# print(student)

mydict1 = {"Name":{
    "School Name":"ABC",
    "Address":"XYZ"
    },
    "Roll Number":25,
    "Section":"C"        
}
# print(mydict1)
# print(mydict1["Name"]["Address"])

mydict = dict({'a' : 'Geeks', 'b' : 'For', 'c' : 'Geeks'})
# print(mydict.get('d', 1))
print(list(mydict.items())[1][1])