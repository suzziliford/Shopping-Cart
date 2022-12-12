

def fill_cart():
    
    cart = {}
    shopping_active = True

    while shopping_active: 
        opening_choice = (input("Would you like to add / remove / view cart / or checkout items?: "))
        if opening_choice == "add":
            a = input("What item would you like to add?: ")
            b = float(input("How much is the item in $?: "))
                # if a in cart:
                #     print("Item already in cart")
                #     c + int(input(" Enter the quantity: "))
                #     cart[a] += c
                # else:
                #     c = int(input("Enter the quantity: "))
                #     cart [a] = c
            c = int(input("How many would you like?: "))
            d = b * c
            cart [a]= b, c, d

        elif opening_choice == "remove":
            to_remove = input("What item would you like to remove?: ")
            if to_remove in cart:
                to_remove = input  
                new_quantity = int(input("How many would you like?"))     
                old_quantity, old_price, old_total = cart[to_remove]
                new_total = new_quantity * old_price
                new_entry = (new_quantity, old_price, new_total)
                cart[to_remove] = new_entry
                
                
                
                # print("Item already in cart.") 
                # b = int(input("Enter the quantity you would you like in total?: "))
                # cart[to_remove] += b, c
            

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

    # for b, c in cart []:
    #     if language["name"]== "Python" and language['proficiency'] >= 7:

    # for key, value in cart.items():
    #     (key)

    total = []    

    for key, value in cart.items():
        total.append(value[2])

    print(sum)    

    #how can I get the dictionary of keys to extrapolate so that I can use that information to calculate the sume of values
    #when dictionary is populated with inputs from a while loop, how do I calculate the total of all the values
    #how to iterate through a dictionary of key-value pairs

    # total_price = sum()   

    # print("All keys from dictionary:", )

    # return x = cart

fill_cart()    
 
