
file = open("demo_text.txt", 'r')
content = file.readlines()
file.close()
for line in reversed(content):
    #print(line)
    with open("demo_text.txt", 'w') as writer:
        for line in reversed(content):
            display = writer.write(line)
            #print(display)

print("-----JSON-----")
import json
contents = '{"name":"rahukshetty", "language":["Java", "Python"]}'
dict = json.loads(contents)
print(type(dict),'\n', dict)
print(dict['language'][0])
print(dict['language'][1])

