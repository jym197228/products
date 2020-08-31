# 讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f: 
# 注意寫入跟讀取的編碼要相同，上一次用utf-8寫入
	for line in f:
		if '商品,價格' in line:
			continue # 繼續、跳到下一迴圈
			#這裡跳過了'商品,價格'，不存入
		name, price = line.strip().split(',') 
		# 先處裡換行符號\n，再針對comma做切割，並且存入name及price
		#存入的部分亦可以做新清單存取{e.g. s = line.strip().split(',')}，但是比複雜，程式會過於笨重
		products.append([name, price]) 
print(products)

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品的價格: ')
    products.append([name, price]) 
    #你也可以存在全新的清單，然後一一存入name和price
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

