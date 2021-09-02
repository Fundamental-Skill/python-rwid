users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": dict(lat="-37.3159", lng="81.1496")
    }
}

print(users)
print("\n")
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])


print(users)
print(type(users))
print("\nUbdah dict ke Json")
import json
result = json.dumps(users)
print(type(result))
print(result)

#Menjadikan file dengan dump
with open("result.json", "w") as file:
    json.dump(users, file)

