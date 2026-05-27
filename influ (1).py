import pandas as pd
data=pd.read_csv('influencer.csv')
month=data["Month"].tolist()
views=data["Views"].tolist()
dislikes=data["Dislikes"].tolist()
subscriber=data["Subscriber(+-)"].tolist()
revenue=data["Revenue"].tolist()
filter=[]

def humble(begin):
    for i in range(len(views)):
        if views[i]<=begin:
            filter.append(month[i])
    print(filter)
    filter.clear()

def golden(age):
    for i in range(len(subscriber)):
        if subscriber[i]>age:
            filter.append(month[i])
    print(filter)
    filter.clear()

def scan(no):
    for i in range(len(revenue)):
        if revenue[i]<=no:
            filter.append(month[i])
    print(filter)
    filter.clear()

#main
scan(0)
