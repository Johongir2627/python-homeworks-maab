# 1. Modifying string with underscores
input_text = input("Enter a string: ")
a = ''
count = 0
vowels = 'aeiou'

for i in range(len(input_text)):
    a += input_text[i]
    count += 1
    if count == 3:
        if input_text[i] in vowels:
            a += input_text[i + 1] if i + 1 < len(input_text) else ''
            a += '_'
            count = 1
        else:
            a += '_'
            count = 0
if a.endswith('_'):
    a = a[:-1]
print(a)








# 2. Integer squares exercise
n = int(input("Enter a number: "))
if n >=1 and n <=20:
    for i in range(n):
        print(i**2)
else:
    print("Invalid number")





