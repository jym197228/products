products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品的價格: ')
    products.append([name, price]) #你也可以創在全新的清單，然後一一存入name和price
print(products)

products[0][0]