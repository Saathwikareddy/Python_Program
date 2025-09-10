cart=[]
print("Cart options: 1. Add Product, 2. Remove Product, 3. Search Product, 4. Display Cart, 5. Count Products,6.Sort,7.Clear")
operations=int(input("Enter the number of times you want to perform the operation"))
for i in range(operations):
    choice=int(input("Enter your choice:"))
    if choice==1:
        n=int(input("Enter th enumber of products to add:"))
        for i in range(n):
            product=input("Enter the product name:")
            cart.append(product)
    elif choice==2:
        product=input("Enter the product name to remove:")
        if product in cart:
            cart.remove(product)
        else:
            print("Product not found")
    elif choice==3:
        product=input("Enter the product to search")
        if product in cart:
            print(f"{product} found")
        else:
            print(f"{product} not found")
    elif choice==4:
        print("Products in the cart are:")
        for i in cart:
            print(i)
        if len(cart)==0:
            print("Cart is empty")
    elif choice==5:
        print(f"Total products in the cart are:{len(cart)}")
    elif choice==6:
        cart.sort()
        print(f"Sorted list:{cart}")
    elif choice==7:
        cart.clear()
        print("Cart is empty")
    else:
        exit()