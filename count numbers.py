numberSentence = input("write a sentence with numbers")

numbers = {
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
    "10" : 0
}
for i in numberSentence:
    if i in numbers:
        numbers[i] += 1


print(numbers)




