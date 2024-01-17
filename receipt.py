#importing datetime module and importing function from sell file
import datetime
from sell import update_laptop

#Importing text file
with open("laptops_details.txt", "r") as file:
    laptops_list = []
    for line in file:
        name, brand, price, stock, processor, gpu = line.strip().split(",")
        laptops_list.append({"name": name, "brand": brand, "price": int(price.replace("$", "")), "stock": int(stock),"processor": processor,"gpu": gpu})
#create a function called file_update with parameters nameoflaptop and quantity
def file_update(nameoflaptop, quantity):
    #assign value to vat and shipping_cost_of_product 0.13 and 0
    vat = 0.13
    shipping_cost_of_product = 0
    manufacturer_name = input("Please, Enter the name of the manufacturer: ")
    for laptop in laptops_list:
        if laptop["name"] == nameoflaptop:
                subtotal_price = quantity * laptop["price"]
                vat_amount = subtotal_price * vat
                total_price = subtotal_price + vat_amount
                laptop["stock"] += quantity
                update_laptop(nameoflaptop, quantity)
                now = datetime.datetime.now()
                #creating a file for receipt
                filename = f"receipt of {nameoflaptop} generated on {now.strftime('%H-%M-%S')}.txt"
                 # write details for receipt
                with open(filename, "w") as receipt:
                    receipt.write(
                         ("----------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                                                                  SUJAL LAPTOP SHOP" "\n" 
                          "----------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                You can find the flagship laptop in our store. Our store has got the best review. Our shop is located at Biratnagar.\n\n"
                          "                                                                                                                     Contact Number: +977-9800000000\n"
                          "----------------------------------------------------------------------------------------------------------------------------------------------------\n"
                          "                                                          Empower your productivity with our laptops.                                               \n"
                          "----------------------------------------------------------------------------------------------------------------------------------------------------\n\n"))
                    receipt.write(f"                                                                                                                  Date of purchase: {now.strftime('%Y-%m-%d')}\n")
                    receipt.write(f"                                                                                                                  Time of purchase: {now.strftime('%H:%M:%S')}\n")
                    receipt.write(f"This receipt belongs to: {manufacturer_name}\n")
                    receipt.write(f"The model of laptop: {laptop['brand']} {laptop['name']}\n")
                    receipt.write(f"The total quantity of laptop ordered: {quantity}\n")
                    receipt.write(f"The price of laptop per unit: ${laptop['price']}\n")
                    receipt.write(f"The subtotal price: ${subtotal_price:.2f}\n")
                    receipt.write(f"The shipping cost of product is: ${shipping_cost_of_product}\n")
                    receipt.write(f"The VAT amount of product with {vat*100}% VAT is: ${vat_amount:.2f}\n")
                    receipt.write(f"The  total price including VAT and shipping cost is: ${total_price:.2f}\n")
                    #print successful message
                print(f"You have successfully bought {quantity} pieces of {nameoflaptop}." "\n" f"Please receive your receipt at {filename}")
                return True
    #print error message
    print(f"The laptop you are looking for {nameoflaptop} is not currently available in our store, or there could be typing error")
    return False
