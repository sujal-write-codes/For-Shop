#importing sell and update_laptop function from, show file, and file_update function from receipt 
from sell import sell, update_laptop
import show
from receipt import file_update

#Importing text file
with open("laptops_details.txt", "r") as file:
    laptops_list = []
    for line in file:
        name, brand, price, stock, processor, gpu = line.strip().split(",")
        laptops_list.append({"name": name, "brand": brand, "price": int(price.replace("$", "")), "stock": int(stock),"processor": processor,"gpu": gpu})

while True:
    #using try and catch
    try: 
        selection = int(input("----------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                                                                       SUJAL LAPTOP SHOP" "\n" 
                          "----------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                You can find the flagship laptop in our store. Our store has got the best review. Our shop is located at Biratnagar.\n\n"
                          "                                                                                                                           Contact Number: +977-9800000000\n"
                          "----------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                                                             Empower your productivity with our laptops.                                                  \n"
                          "----------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "Please read this information for you ease..\n\n"
                          "Do you want to buy laptop from us, Type 1!! \n"
                          "Do you want to purchase laptop from manufacturer, Type 2!! \n"
                          "Do you want to see the details of laptop, type 3!! \n"
                          "Do you want to exit the program or terminal, Type 4!! \n"
                          "What do you want to do? Please type number according to your need: "))

    except ValueError:
        #print error message
        print("Invalid input! Please enter an integer value.")
        continue
  

        #make choices for user
    if selection == 1:
        print("These are the kinds of laptops that are available in our shop, Please type the name of laptop you want to buy: ")
        for laptop in laptops_list:
            print(f"Laptop Name:{laptop['name']:15} Price:${laptop['price']}")
        nameoflaptop = input("If you are interested!! \nPlease type the name of laptop you are willing to buy: ")
        while True:
            try: 
                quantity = int(input("How many pieces of laptop you want to buy: "))
                if quantity <= 0:
                    print("The pieces of laptop cannot be negative value or 0.")
                    continue
                break
            except ValueError as error:
                print(f"The input you gave is invalid, Try using integer value!!!")
        sell(nameoflaptop, quantity)

    elif selection == 2:        
        print("These are the kinds of laptops that are available in our shop")
        for laptop in laptops_list:
            print(f"Laptop Name:{laptop['name']:15} Price:${laptop['price']}")
        nameoflaptop = input("Please type the name of laptop you are willing to buy from manufacturer: ")
        while True:
            try:
                quantity = int(input("How many pieces of laptop you want to update: "))
                if quantity <= 0:
                    print("The pieces of laptop cannot be negative value or 0.")
                    continue
                break
            except ValueError as error:
                print(f"The input you gave is invalid: {error}, Try using integer value!!!")
        file_update(nameoflaptop, quantity)

    # Display the details of laptops 
    elif selection == 3:
        print(show.show())

        #exit programs
    elif selection == 4:
        exit("The program has been terminated!!!")
        
    else:
        print(f"You have choose number {selection} which exceeds than the given number in the program \n"
              "Please Read the information given above!!")
