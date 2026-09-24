
Product_Name_one = input("enter the product name one")
Product_Name_two = input("enter the product name two")

Prodcut_price_one = int(input("enter the product price one"))
Prodcut_price_two = int(input("enter the product price two"))

product_quantity_one = int(input("enter the quantity one"))
product_quantity_two = int(input("enter the quantity two"))

product_total_one = Prodcut_price_one  * product_quantity_one
product_total_two = Prodcut_price_two  * product_quantity_two




total = product_total_one +product_total_two

print(f"this is product one {Product_Name_one} and that is product one total {product_total_one}")
print(f"this is product two {Product_Name_two} and that is product two total {product_total_two}")
print(f"total all of product one or two is {total}")