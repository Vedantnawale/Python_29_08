dict = {
    "name":"Vedant",
    "sname":"Nawale"
}
# print(dict["name"]) 
# print(dict.keys())
# print(dict.values())
# print(dict.get("name"))

# for i in dict.keys():
#     print(f"for the key {i} the value is {dict[i]}")

print(dict.items())
for key,value in dict.items():
    print(f"The corresponding value of {key} is {value}")
