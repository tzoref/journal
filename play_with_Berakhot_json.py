
# Create a text file of the textual material in the json Berakhot file that will be usable for text analysis


import json

with open('Berakhot_sefaria.json') as f:
    data = json.load(f)

# print data to examine its content.  Comment out this code to reduce volume of output.
# print(data)

# print type of data.  Output is: class 'dict'
print("Type of data = " + str(type(data)))

# print the keys of the dictionary, data
print(data.keys())
print("")
# output is: dict_keys(['language', 'title', 'versionSource', 'versionTitle', 'status', 'priority', 'license', 'licenseVetted', 'versionNotes', 'versionTitleInHebrew', 'versionNotesInHebrew', 'heTitle', 'categories', 'text', 'sectionNames'])

# print the type of the keys
for key in data.keys():
    print("The Type of " + key + " is: " + str(type(data[key])))
    print("")

# print the values of the keys, separating keys of type string, floar, and boolean
for key in data.keys():
    if type(data[key]) == str:
        print("Value of " + key + ": " + (data[key]))
        print("")
    elif type(data[key]) == float:
        print("Value of " + key + ": " + str((data[key])))
        print("")
    elif type(data[key]) == bool:
        print("Value of " + key + ": " + str((data[key])))
        print("")
    else:
        print("Type of " + key + ": " + str(type(data[key])))

# output: 'categories', 'text', and 'sectionNames' are lists

# print length of the keys that are lists
print(len(data['categories']))  # output: 3
print(len(data['text']))        # output: 127
print(len(data['sectionNames'])) # output: 2

# print the values for categories and sectionNames
for c in data['categories']:
    print(c)
# output: Talmud, Bavli, Seder Zeraim

for sectionN in data['sectionNames']:
    print(sectionN)
# output: Daf, Line

# set a variable for the contents of the 'text' key
text_list = data['text']
print(len(text_list))
print(type(text_list))

print(text_list)

# retrieve the values for the individual elements in the list "text_list"
for i in text_list:
    print(i)
    print(len(i))
    print(type(i))
    print("")

print(text_list[0])
print(text_list[1])
test_paragraph = (text_list[7])
print(len(test_paragraph))
print(test_paragraph[0])
for word in test_paragraph:
    for letter in word:
        print(letter)

for paragraph in text_list:
    for word in paragraph:
        for letter in word:
            print(letter)
            