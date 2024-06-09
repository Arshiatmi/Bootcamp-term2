data = [
    {
        "name":"Arshia",
        "age":23,
        "scores":[5,20,18],
        "allowed_in":[
            {"id":1,"city":"ramsar"},
            {"id":2,"city":"tehran"},
        ]
    },
    {
        "name":"Ali",
        "scores":[15,20,18],
        "allowed_in":[
            {"id":3,"city":"rasht"},
            {"id":4,"city":"lahijan"},
        ]
    },
]

index = input("Enter What You Want? ").lower().strip()

for i in data:
    try:
        print(i[index])
    except KeyError:
        print("This Key Is Not Valid :/")






data = [
    {
        "name":"Arshia",
        "age":23,
        "scores":[5,20,18],
        "allowed_in":[
            {"id":1,"city":"ramsar"},
            {"id":2,"city":"tehran"},
        ]
    },
    {
        "name":"Ali",
        "scores":[15,20,18],
        "allowed_in":[
            {"id":3,"city":"rasht"},
            {"id":4,"city":"lahijan"},
        ]
    },
]

new_score = input("Enter New Score Of Arhsia: ")

try:
    new_score = int(new_score)
    if (new_score < 0 or new_score > 20):
        raise
except:
    print("You Must Enter Valid Score :/")
    exit(1)

data[0]["scores"].append(new_score)
print(data[0]["scores"])
