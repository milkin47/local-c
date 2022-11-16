class base():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Father name and age: ", self.name, self.age)
class derived(base):
    # def __init__(self, name2, age2):
    #     self.name2 = name2
    #     self.age2 = age2
    # def display3(self):
    #     print("Test:", self.name2, self.age2)

    def child(self, name1, age1):
        self.name1 = name1
        self.age1 = age1
    def display_child(self):
        print("Son name and age: ", self.name1, self.age1)
obj = derived("sekar", 40)
obj.display()
obj.child("karthick", 20)
obj.display_child()

s = ['all', 'the', 'best']
string = " ".join(s)
#string1 =
print(string)

print("----dictionary-----")
print("--merging keys and values---")
dic1 = ['a', 'b', 'c', 'd']
dic2 = [10,20,30, 40]
#dic3 = [3, 4, 6, 5]
final = dict(zip(dic1, dic2))
print("final dic: ", final)

print("-- merging two dics---")
a = {'ab':100, 'bc':200, 'cd':60000}
b = {'cd':300, 'de':400, 'ef':500}
#c = {**a, **b}
c = a.copy()
c.update(b)
print(c)
a['ze'] = a.pop('ab')
print(c)
print("--printing keys----")
for i in c.values():
    if 200 == i:
        print("keys: ", c.keys())


sampleDict = {
    "class": {
         "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"])
print(sampleDict['class']['student'])
print(sampleDict['class']['student']['marks'])
print(sampleDict['class']['student']['marks']['physics'])
print("-----for loop----")
for i in sampleDict.values():
    print(i)
    if 70 in i:
        print("keys: ", sampleDict.keys())

print("--mapping keys and values----")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
map = dict.fromkeys(employees, defaults)
print("map: ",map)

list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
#res = [(val, pow(val, 3)) for val in list1]
res = []
for val in list1:
    c = [val, pow(val, 3)]
    res.append(tuple(c))
print("res: ", res)

res_tuple = tuple(res)
print("res_tuple:", res_tuple)

print("---Iterators-----")
mylist = [100, 200, 300, 400]
loop = iter(mylist)
print(next(loop))
print(next(loop))
print(loop.__next__())







