name=str(input("Enter the string:"))
vowelcount=0
consonantcount=0
for i in name:
    if i in 'aeiouAEIOU':
        vowelcount+=1
    elif i.isalpha():
        consonantcount+=1
print(f"Number of vowels in {name} are:{vowelcount}")
print(f"Number of consonants in {name} are:{consonantcount}")
