kilo = int(input("Kilometer : "))
if(kilo>0):
    print(kilo,"Pass")
else:
    print(kilo,"Cannot Calculate")
time = int(input("Time : "))
if(time>0):
    print(time,"Pass")
else:
    print(time,"Cannot Calculate")
result = kilo/time
print(result,"km/h")


