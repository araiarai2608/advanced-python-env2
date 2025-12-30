a = input()
open = a.find("(")
close = a.find(")")

print(a[open+1:close])
