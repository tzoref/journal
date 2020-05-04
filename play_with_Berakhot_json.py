
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
for element in text_list:
    print(element)
    print(len(element))
    print(type(element))
    print("")

# output: each element is a list

print(text_list[0])
print(text_list[1])
print(text_list[3])
print(text_list[126])
print(len(text_list[3]))
print(len(text_list[126]))

test_element = text_list[3]
print(len(test_element))
print(test_element[0])
print(type(test_element[0]))

# the elements in the list are strings

string_text = ""
for element in text_list:
    for string in element:
        for letter in string:
            print(letter)
            string_text = letter + string_text
print(string_text)
print(type(string_text))
print(len(string_text))

    


#for i in range(126):
    #text_element = text_list[i]
    ##calculate the length of each text_element list
    ## isolate the values in the element list, and identify their type
    ## since the type output is string, i have named the variable "string_element"
    #for s in range(counter):
        ##string_element = text_element[s]
        #print(string_element)
        ##print(type(string_element))
        
        # isolate the letters in the strings
        #letter = " "
        #for l in string_element:
            #letter += l
#print(letter)
#print(type(letter))
#print(len(letter))
