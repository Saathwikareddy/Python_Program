def digit_to_word(ch):
    if ch == "0": return "Zero"
    elif ch == "1": return "One"
    elif ch == "2": return "Two"
    elif ch == "3": return "Three"
    elif ch == "4": return "Four"
    elif ch == "5": return "Five"
    elif ch == "6": return "Six"
    elif ch == "7": return "Seven"
    elif ch == "8": return "Eight"
    elif ch == "9": return "Nine"

num = input("Enter a number: ")

print("In words:", end=" ")

for ch in num:
    print(digit_to_word(ch), end=" ")
