with open("laptops_details.txt", "r") as file:
    laptops_list = []
    for line in file:
        name, brand, price, stock,processor,gpu = line.strip().split(",")
        laptops_list.append({"name": name, "brand": brand, "price": int(price.replace("$", "")), "stock": int(stock),"processor": processor,"gpu":gpu})

def show():
    for laptop in laptops_list:
         print(f"Laptop Name: {laptop['name']:15} Laptop Brand: {laptop['brand']:10} Laptop Price:${laptop['price']:4}  Stock: {laptop['stock']}  Processor:{laptop['processor']}  GPU:{laptop['gpu']}")
