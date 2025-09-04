def get_number():
    n = int(input("Enter a number: "))
    return n

z = get_number()


last_digit = z % 10

while z >= 10:
    z //= 10  
first_digit = z

print("First digit:", first_digit)
print("Last digit:", last_digit)

