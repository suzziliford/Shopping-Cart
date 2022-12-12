
def fill_cart():
    
    cart = {}
    
    shopping_active = True
    
    while shopping_active: 
        opening_choice = (input("Would you like to add / 'remove / view (items in cart) / or checkout items?: ")).lower().strip()
        if opening_choice == "add":
            a = (input("What item would you like to add?: "))
            b = float(input("How much is the item in $?: "))
            c = int(input("How many would you like?: "))
            d = b * c
            cart [a]= a, c, b, d

        elif opening_choice == "remove":
            to_remove = input("What item would you like to remove?: ")
            if to_remove in cart:
                new_quantity = int(input("How many would you like in total?"))     
                old_name, old_quantity, old_price, old_total = cart[to_remove]
                new_total = new_quantity * old_price
                new_entry = (old_name, new_quantity, old_price, new_total)
                cart[to_remove] = new_entry
                

        elif opening_choice == "view":
            for a in cart:
                print(a, ":", cart[a])


        elif opening_choice == "checkout":
            shopping_active = False
            print("Proceeding to check out")

    
        elif opening_choice != "add" "remove" "view" "checkout":
            print("please try a word from the list")
    
    total = []  
    
    for key, value in cart.items():
        total.append(value[3]) 

    itemized_list = []

    for value in cart.items():
        itemized_list.append(value[:])

    # for tup in itemized_list:
    #     print (f'{tup[1]} x {tup[2]} at $ {tup[3]} = {tup[3]}')    
   
    print(itemized_list)


    amount_due = sum(total)
    
    print("Total = $" + str(amount_due))
  
fill_cart()    
 
