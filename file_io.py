import json
# 

data = [{"name": "",
        "age": 0,
        "occupation": ""},

        {"name": "",
        "age": 0,
        "occupation": ""},

        {"name": "",
        "age": 0,
        "occupation": ""}]

data[0]["name"] = input("enter your name: ")
data[0]["age"] = int(input("enter your age: "))
data[0]["occupation"] = input("enter your occupation: ")


file = open("user.json", "w")

json.dump(data, file, indent=4)