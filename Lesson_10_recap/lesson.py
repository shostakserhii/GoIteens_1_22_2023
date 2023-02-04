import random

random_int = random.randint(1, 10)
print(random_int)

print(random.choice(["a", 1, True, 'b', 'awdawd']))
print(random.choices(['a', 'b', 'c', 'd', 'e', 'f'], k=3))


length = 5
my_empty_list = []

for number in range(length):
    my_empty_list.append(random.randint(1, 10))

print(my_empty_list)


l1 = [1, 20, 3, 4, 5]
l2 = [2, 5, 10, 11, 1]

for i in l1:
    print(i)


password = "dawd"

is_len = False
is_upper = False

if len(password) >= 8:
    is_len = True

if password[0].isupper():
    is_upper = True

if is_len and is_upper:
    print("nice password!")
else:
    print("Missing:")
    if not is_len:
        print(" - Not enough symbols")
    if not is_upper:
        print(" - Upper letter missing")

i = 0

while i < 10:
    print(i)
    i += 1

if 4 % 2 == 0 and 12 % 3 == 0:
    print("number!")

l3= ['a', 'b', 'c']
for x, y in enumerate(l3):
    print(x, y)


