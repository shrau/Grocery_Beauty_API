import itertools
class Cart:
    def __init__(self):
        self.item_list_grocery=[{"Item_name":"Milk","Item_no":101,"Item_stock":30,"Item_price":30},
                        {"Item_name":"Bread","Item_no":102,"Item_stock":34,"Item_price":35},
                        {"Item_name":"Biscuit","Item_no":103,"Item_stock":20,"Item_price":25},
                        {"Item_name":"Snacks","Item_no":104,"Item_stock":27,"Item_price":45},
                        {"Item_name":"Ghee","Item_no":105,"Item_stock":40,"Item_price":450},
                        {"Item_name":"Jam","Item_no":106,"Item_stock":17,"Item_price":15},
                        {"Item_name":"Choclates","Item_no":107,"Item_stock":50,"Item_price":50},
                        {"Item_name":"Icecream","Item_no":108,"Item_stock":42,"Item_price":60},
                        {"Item_name":"Cheese","Item_no":109,"Item_stock":55,"Item_price":75},
                        {"Item_name":"Butter","Item_no":110,"Item_stock":15,"Item_price":40}]
        
        self.item_list_beauty=[{"Item_name":"Sunscreen","Item_no":201,"Item_stock":36,"Item_price":300},
                        {"Item_name":"Bodylotion","Item_no":202,"Item_stock":34,"Item_price":100},
                        {"Item_name":"Lipbalm","Item_no":203,"Item_stock":25,"Item_price":80},
                        {"Item_name":"Foundation","Item_no":204,"Item_stock":45,"Item_price":635},
                        {"Item_name":"Concealer","Item_no":205,"Item_stock":22,"Item_price":345},
                        {"Item_name":"Lipstick","Item_no":206,"Item_stock":15,"Item_price":550},
                        {"Item_name":"Kajal","Item_no":207,"Item_stock":25,"Item_price":150},
                        {"Item_name":"Primer","Item_no":208,"Item_stock":32,"Item_price":250},
                        {"Item_name":"Eyeshadow","Item_no":209,"Item_stock":19,"Item_price":200},
                        {"Item_name":"Fixer","Item_no":210,"Item_stock":43,"Item_price":300}]

    
        
    def check_item_grocery(self):
        return self.item_list_grocery
    

    def check_item_beauty(self):
         return self.item_list_beauty
    
    
    def product_detail(self,Item_name):
            try:
                for grocery_item,beauty_item in itertools.zip_longest(self.item_list_grocery,self.item_list_beauty):
                    if grocery_item and grocery_item["Item_name"]==Item_name:
                        return {
                             'status':'Success',
                             'result':f"Details of your product={grocery_item}"
                        }
                    elif beauty_item and beauty_item["Item_name"]==Item_name:
                        return {
                            'status':'Success',
                            'result':f"Details of your product={beauty_item}"
                        }
                else:
                    return{
                        'status':'Failed',
                        'result':f"{Item_name} is not available"
                        }
                    
      
            except Exception as e:
                return{
                      'status':'Failed',
                      'result': str(e)
                 }
            
            
    def check_stock(self,Item_name):
        for grocery_item, beauty_item in itertools.zip_longest(self.item_list_grocery,self.item_list_beauty):
            if grocery_item["Item_name"]==Item_name:
                return f"Your Product {Item_name} with it's stock ={grocery_item['Item_stock']}"
            
            elif beauty_item["Item_name"]==Item_name:
                return f"Your Product {Item_name} with it's stock = {beauty_item['Item_stock']}"
        else:
            return{
                    'status':'Failed',
                    'result':f"{Item_name} is not available to check stock"
                    }
        
                
    def check_price(self,Item_name,Quantity):
        for grocery_item,beauty_item in itertools.zip_longest(self.item_list_grocery,self.item_list_beauty):
            if grocery_item["Item_name"]==Item_name:
                total_price=grocery_item["Item_price"]* Quantity
                return f"Total price of {Item_name} is {total_price}"
            
            elif beauty_item["Item_name"]==Item_name:
                total_price=beauty_item["Item_price"]* Quantity
                return f"Total price of {Item_name} is {total_price}"


    def buy_grocery(self,Item_name,Quantity):
        for check_item in self.item_list_grocery:
            if check_item["Item_name"]==Item_name:
                if check_item["Item_stock"]>Quantity: 
                    check_item["Item_stock"]-=Quantity
                    return f"The updated stock is {check_item['Item_stock']}"
                elif check_item["Item_stock"]<Quantity:
                    return f"out of stock,stock of {check_item['Item_name']} is {check_item['Item_stock']}"
                elif check_item["Item_stock"]==Quantity:
                    check_item["Item_stock"]-=Quantity
                    return f"The stock is empty {check_item['Item_stock']}"
                
                
    def add_item(self,item_name,item_no,item_stock,item_price):
        try:
            new_item={
                        "item_name":item_name,
                        "item_no":item_no,
                        "item_stock":item_stock,
                        "item_price":item_price
                    }
            self.item_list_grocery.append(new_item)
            return{
                    'status':"Success",
                    'result': f"The list updated by following details :{item_name},{item_no},{item_stock},{item_price}"
            }

        except Exception as e:
            return {
                'status': 'Failed',
                'result': str(e)
            }
        
    def buy_product(self,Item_name,Quantity):
        for check_item in self.item_list_grocery:
            if check_item["Item_name"]==Item_name:
                total_price=check_item["Item_price"]*Quantity
                return f"Total price of {Item_name} is {total_price}"
        



        
                

                






        

    

