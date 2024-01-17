#importing datetime module
import datetime 

#Importing text file
with open("laptops_details.txt", "r") as file:
    laptops_list = []
    for line in file:
        name, brand, price, stock, processor, gpu = line.strip().split(",")
        laptops_list.append({"name": name, "brand": brand, "price": int(price.replace("$", "")), "stock": int(stock),"processor": processor,"gpu": gpu})

#create a function called sell with parameters nameoflaptop and quantity
def sell(nameoflaptop, quantity):
    #assign shipping_cost_of_product to 0
    shipping_cost_of_product = 0
    customer_name = input("Please, Enter your name: ")
    shipping_details = input("Do you wish to ship the laptop in your designated place?" "\n" "Type 'yes' for shipping or if you don't want shipping type 'no': ")
    if shipping_details == 'yes':
        shipping_cost_of_product = 100
    for laptop in laptops_list:
        if laptop["name"] == nameoflaptop:
            if laptop["stock"] >= quantity:
                subtotal_price = quantity * laptop["price"]
                total_price = subtotal_price + shipping_cost_of_product
                laptop["stock"] -= quantity
                update_laptop(nameoflaptop, quantity)
                now = datetime.datetime.now()
                # create a file for receipt
                file_for_receipt = f"receipt of {nameoflaptop} generated on {now.strftime('%H-%M-%S')}.txt"
                # write details for receipt
                with open(file_for_receipt, "w") as a:
                    a.write(
                         ("----------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                                                                  SUJAL LAPTOP SHOP" "\n" 
                          "----------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                You can find the flagship laptop in our store. Our store has got the best review. Our shop is located at Biratnagar.\n\n"
                          "                                                                                                                     Contact Number: +977-9800000000\n"
                          "----------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                                                          Empower your productivity with our laptops.                                               \n"
                          "----------------------------------------------------------------------------------------------------------------------------------------------------\n\n"))
                    a.write(f"                                                                                                                  Date of purchase: {now.strftime('%Y-%m-%d')}\n")
                    a.write(f"                                                                                                                  Time of purchase: {now.strftime('%H:%M:%S')}\n")
                    a.write(f"This receipt belongs to: {customer_name}\n")
                    a.write(f"The model of laptop: {laptop['brand']} {laptop['name']}\n")
                    a.write(f"The total quantity of laptop ordered: {quantity}\n")
                    a.write(f"The price of laptop per unit: ${laptop['price']}\n")
                    a.write(f"The subtotal price: ${subtotal_price:.2f}\n")
                    a.write(f"The shipping cost of product is: ${shipping_cost_of_product}\n")
                    a.write(f"The  total price including VAT and shipping cost is: ${total_price:.2f}\n")
                # print success message
                print(f" \nYou have successfully bought {quantity} pieces of {nameoflaptop}." "\n" f"Please receive your receipt at {file_for_receipt}")
                return True
            else:
                # print information message
                print("The laptop is currently out of stock, Wait until the laptop restocks.")
                return False
            # print error message
    print(f"\nThe laptop you are looking for {nameoflaptop} is not currently available in our store, or there could be typing error")
    return False

# create a function called update_laptop
def update_laptop(laptop_name, quantity):
    for laptop in laptops_list:
        if laptop["name"] == laptop_name:
            laptop["stock"] += quantity
            with open("laptops_details.txt", "w") as file:
                for laptop in laptops_list:
                    file.write(f"{laptop['name']},{laptop['brand']},{laptop['price']},{laptop['stock']},{laptop['processor']},{laptop['gpu']}\n")
            return True
    return False


