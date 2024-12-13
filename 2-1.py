from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
x=pd.DataFrame(iris['data'], columns=iris['feature_names']) #columns為橫坐標    
y=pd.DataFrame(iris['target'], columns=['target'])
y1=pd.DataFrame(pd.Series(iris['target']).map(dict(enumerate(iris['target_names']))), columns=['target_name']) # .map(dict(enumerate(iris['target_names']))) 將 Series 中的每個元素（類別編碼）映射為對應的花卉品種名稱

print(x)
print(y)
print(pd.concat([x,y1],axis=1))#合併兩個數據
