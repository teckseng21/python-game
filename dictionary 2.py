input_value=input("Enter the string-")
vowels={"a":0,"e":0,"i":0,"o":0,"u":0}

for c in input_value:
    if c in vowels:
        vowels[c]=vowels[c]+1
print (vowels)

word_count=0
character_count=0
for c in input_value:
    word_count+=1
    if c.isalpha():
        character_count+=1
print (character_count)

print (word_count)

number=input("Enter the number")

number_count={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

for num in number:
    if num in number_count:
        number_count[num]+=1
print (number_count)
panagram=True
for count in number_count.values():
    if count==0:
        panagram=False

if panagram:
    print ("Entered number is a panagram!")
else :
    print ("Entered number is not a panagram!")