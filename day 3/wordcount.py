statement=str(input("Enter the string:"))
words=statement.split()
wordcount=0
for word in words:
    wordcount+=1
print(f"Number of words in the given string are:{wordcount}")