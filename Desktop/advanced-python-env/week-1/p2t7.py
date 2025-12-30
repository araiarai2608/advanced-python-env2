a = input()
b = len(a) // 2
a = a[:b].replace("n", "*") + a[b:]
print(a)
