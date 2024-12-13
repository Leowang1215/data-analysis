import pandas as pd
fruits = ['apple', 'banana', 'cherry']
number = ['0','1','2']
# 1. enumerate列舉用法
for index,value in enumerate(fruits): #eumerate某東西後會得到兩個值，像是以上的範例(0,apple),(1,banana)... index和value會分別取得第一個數字和第二個水果的名字
    print(index,value)
# 2. python 內建 map用法
    def square(x):
        return x * x

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)  # 創建 map 對象

    print("type:", type(squared_numbers))
    # 將 map 對象轉換為列表並打印
    squared_list = list(squared_numbers)
    print(squared_list)  # [1, 4, 9, 16, 25]

    # 再次嘗試遍歷同一個 map 對象（已經被耗盡）(map return的迭代器只能被遍歷一次)
    print(list(squared_numbers))  # []
# 3. pandas 內建map用法
    # 創建一個 Series
    s = pd.Series([1, 2, 3, 4])
    # 將每個元素加上 10
    mapped_s = s.map(lambda x: x + 10)
    print(mapped_s)