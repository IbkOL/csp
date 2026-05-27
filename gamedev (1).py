import pandas as pd
data=pd.read_csv('gamedev.csv')
level=data["Level"].tolist()
time=data["Time"].tolist()
rating=data["Rating"].tolist()
summary=data["Summary"].tolist()
feedback=data["Feedback"].tolist()
filter=[]

def bad(level_rating):
    for i in range(len(rating)):
        if rating [i]<level_rating:
            filter.append([i])
    print(filter)
    filter.clear()

def view(timing,rates):
    for i in range(len(time)):
        if time[i]>timing and rating [i]>rates:
            filter.append([i])
    print(filter)
    filter.clear()

def result(final):
    for i in range(len(feedback)):
        if final in feedback[i]:
            filter.append([i])
    print(filter)
    filter.clear()
#main
bad(1.5)
view(500,4)
result("secret")
print(data.loc[[34,77]])
print(data.loc[[79]])
print(data.loc[[66]])


