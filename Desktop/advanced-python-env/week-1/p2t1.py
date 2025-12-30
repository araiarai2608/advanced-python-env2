a = input()
words = a.split()
count = 0
for i in words:
    if i.startswith("e"):
        count += 1

print(count)