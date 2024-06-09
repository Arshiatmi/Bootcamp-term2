data = [
    {
        "name":"Arshia",
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

print(data[0]["allowed_in"][0]["city"]) # ramsar
print(data[0]["scores"][1]) # 20
