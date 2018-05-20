#设计一个程序  结合自己喜欢的菜谱  使用网上的蔬菜报价优化出每日的推荐菜    如果可以结合运筹学  给出每日需要提前是否腌制准备酱料等等

import  csv




#菜谱录入采用csv

import csv

filename = 'caidan.csv'
with open(filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Max TemperatureF是表第一行的某个数据，作为key
        max_temp = row['菜名']
        print(max_temp)



#菜价获取












#运筹优化