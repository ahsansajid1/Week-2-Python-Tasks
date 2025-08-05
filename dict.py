# Student record CRUD in dict.

student ={
    "name" :"Ahsan",
    "marks":[34,55,89],
    "Roll No": 123
}

student["section"]= "Blue"
student["marks"]= [34,66,91]
del student["name"]
print(student, "\n")

# Count word frequency in sentence.

sentence= "his name is Ahsan . Ahsan is very good Man"

split= sentence.split()

word_count={}

for word in split:
    word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
 
for word, count in word_count.items():
    print(f"{word} → {count}")