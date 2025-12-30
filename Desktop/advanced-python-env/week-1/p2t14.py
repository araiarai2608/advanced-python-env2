a = input()
words = a.split()
for i in words:
    if i.startswith("a") or i.endswith("i"):
        print(i)
