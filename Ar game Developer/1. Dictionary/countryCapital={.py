countryCapital={
    "US" : "washington DC",
    "germany" : "berlin",
    "china" : "beijing",
    "italy" :"rome"
}

countryCapital["US"] = "london"

print (countryCapital)

if "china" in countryCapital :
    print("it is present")

else :
    print ("key is not present")

countryCapital["italy"] = "barcelona"
print(countryCapital)

del countryCapital["germany"]
print(countryCapital)

print(countryCapital.keys())

print(countryCapital.values())

print (countryCapital)

for key in countryCapital.keys():
    print(key,countryCapital[key])





