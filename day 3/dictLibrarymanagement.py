dict={}
n=int(input("Enter the number of books:"))
for i in range(n):
    BookID=int(input("Enter the Book ID:"))
    BookTitle=input("Enter the Book title")
    dict[BookID]=BookTitle
print("Enter the bookId to delete:")
id=int(input())
if id in dict:
    del dict[id]
    print("Book is deleted")
print("Enter the bookid to search:")
id1=int(input())
if id1 in dict:
    print(f"Book is present:{dict[id1]}")
else:
    print("Book is not present")
print("Enter the book id to update:")
id2=int(input())
dict[id2]=input("Enter the new title:")
print(f"All the books in the library are:{dict.values()}")
print(f"Total number of books in the library are:{len(dict)}")
print("Enter the book title to search:")
title=input()
if title in dict.values():
    print("Book is present")
else:
    print("Book is not present")