# 檢查想讀取之檔案是否存在
import os #operating system
# 讀取檔案
def read_file(filename):
    products = []    
    with open(filename, 'r', encoding = 'utf-8') as f: 
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
    return products
# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品的價格: ')
        products.append([name, price]) 
        #你也可以存在全新的清單，然後一一存入name和price
    print(products)
    return products
# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])
# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

    #檢查檔案在不在
# 程式的進入點
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        # 上面亦可以用絕對路徑
        print('檔案存在')
        products = read_file(filename)
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()