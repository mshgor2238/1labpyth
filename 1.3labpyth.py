a = ' #лЯ #лЯ #ля '
print(a, id(a))
a = a.strip()
print(a, id(a))
a = a.lower()
print(a, id(a))
a = a.replace('я', 'яяяяя')
print(a, id(a))
print(a, id(a))