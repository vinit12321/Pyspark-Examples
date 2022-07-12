
s={
    "name":"vinit",
    "age":"23",
    "gender":"Male",
    
}

'''

print(s.get("name"))
print(s)
s["name"]="VinitD."
print(s)

'''

numbers={
    "1":"One",
    "2":"two",
    "3":"Three"
}

num=input("Enter the Phone Number: ")
print(num)
keys=list(num)
print(keys)
for i in keys:
    print(numbers.get(i),end="|")
