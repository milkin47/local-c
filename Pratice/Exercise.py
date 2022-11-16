weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)
print(weekdays.count('mon'))

list = ['a', 'b', 'c', 'def']
s = "".join(list)
print(s)

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])
for x in weekdays:
    print([x, weekdays.count(x)])

data = lambda num: num%2==0
print(data(12))
