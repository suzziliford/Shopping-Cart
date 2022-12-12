

# choice = input ("Would you like to add/remove item or checkout?")   
# # if choice == "checkout":
# #     break
    
# if choice == "add":
#         print (input "Which item would you like to add?")

# if choice == "remove":
#         print ("Which item would you like to remove?")    

def fill_cart():
    
    cart = {}
    shopping_active = True

    while shopping_active: 
        opening_choice = (input("Would you like to add / remove / view cart / or checkout items?: "))
        if opening_choice == "add":
            a = input("What item would you like to add?: ")
            b = int(input("How much is the item in $?: "))
                # if a in cart:
                #     print("Item already in cart")
                #     c + int(input(" Enter the quantity: "))
                #     cart[a] += c
                # else:
                #     c = int(input("Enter the quantity: "))
                #     cart [a] = c
            c = int(input("How many would you like?: "))
            cart [a]= b, c
            #need to add an if statement to avoid over riding if they want to add more of the same items
            # added_item = { [added_item]} 
            # [added_item] = added_price 
            # cart [quantity] = quantity 
            # cart["product"]

        elif opening_choice == "remove":
            to_remove = input("What item would you like to remove?: ")
            if to_remove in cart:
                print("Item already in cart.") 
                c = int(input("Enter the quantity you would you like in total?: "))
                cart[a] += b, c

            else:
                del(cart[to_remove])
                print(to_remove,"has been removed")
            # for product in cart:
            #     if to_remove == product:
            #         print(cart[product][a][b][c])

                    # print(product() for product in cart if (quantity)<=1)
            
            
            
            
            
            # for key, val in product.items():
            #     print(product[key][val][key][val]['key']['val'])
            #     if [c] >= 1:
            #         input("How many would you like to remove?: ")

            #     else:
            #         del x

                    #is it a pop situation?
            # for x in cart:
            #     if x cart[i][quantity]
            # if [c] > 1:
            #     num_to_remove = input("How many would you like to remove?")
            #     c - num_to_remove
                
            # else remove(product)

                # else:
                #     remove.x
            # for x in cart.items:
            # del cart [to_remove]
            # for to_remove in cart:

        elif opening_choice == "view":
            # for (f"{key} for ${val}")
            for a in cart:
                print(a, ":", cart[a])


        elif opening_choice == "checkout":
            shopping_active = False
            print("Proceeding to check out")

    
        elif opening_choice != "add" "remove" "view" "checkout":
            print("please try again fumble-fingers")
    # for items in cart:

    

    # return x = cart

fill_cart()    
 
# for product, price, quantity, in cart.items():
#     #calculate total price
#     print(f'{product} $ {price} x {quantity}')

# for items in cart:
    
#     print(f'{product()}  ${price()} {quantity}')