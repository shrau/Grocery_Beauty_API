from service.cart.cart import Cart
c1=Cart()
while True:
    op=int(input("Please select your choice\n1.Products\n2.Specific Product Detail\n3.To check Stock\n4.Check Price\n5.Buy Grocery\n6.Add item\n7.Buy Product\n"))
    if op==1:
        op=int(input("Please select\n1.Grocery\n2.BeautyProducts\n"))
        if op==1:
            print(c1.check_item_grocery())
        elif op==2:
            print(c1.check_item_beauty())
    elif op==2:
        Item_name=input("please enter the item name\n").capitalize()
        print(c1.product_detail(Item_name))
    elif op==3:
        Item_name=input("please enter the item name\n").capitalize()
        print(c1.check_stock(Item_name))
    elif op==4:
        Item_name=input("please enter the item name\n").capitalize()
        Item_quantity=int(input("please enter the quantity\n"))
        print(c1.check_price(Item_name,Item_quantity))
    elif op==5:
        Item_name=input("please enter the item name\n").capitalize()
        Item_quantity=int(input("please enter the quantity\n"))
        print(c1.buy_grocery(Item_name,Item_quantity))

    elif op==6:
        Item_name,Item_no,Item_stock,Item_price=input("please add product details\n").split(',')
        print(c1.add_item(Item_name.capitalize(),int(Item_no),int(Item_stock),int(Item_price)))








