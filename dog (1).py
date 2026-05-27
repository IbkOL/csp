import pandas as pd
data=pd.read_csv('dog.csv')
name=data["Name"].tolist()
mini=data["Minimum Weight"].tolist()
maxi=data["Maximum Weight"].tolist()
temperament=data["Temperament"].tolist()
image=data["Image"].tolist()
bredfor=data["BredFor"].tolist()
import webbrowser

filter=[]

#Init


#Function
def pound(we):
    print("Hi what size dog are you looking for tiny,small,meduim, or large")
    we=input("what size dog are you looking for")
    if "tiny"==we:
        print("these dogs would be a good fit")
        for i in range(len(mini)):
            if mini[i]<=10:
                filter.append(name[i])
    elif"small"==we:
        print("these types of dogs would be a good fit")
        for i in range(len(mini)):
            if mini[i]<=25 and 11:
                filter.append(name[i])
    elif "medium"==we:
        print("I think these dogs would be a good fit")
        for i in range(len(mini)):
            if mini[i]<=60 and 26:
                filter.append(name[i])
    else:
        print("these are the types of dogs i would choose for you")
        for i in range(len(mini)):
            if mini[i]>=60:
                filter.append(name[i])
    print(filter)
    print("these dogs will fit you best")
    filter.clear()


def tone(ima):
    index="no"
    ima=input("what kind of temperament do you want the dog to have")
    for i in range(len(name)):
        if name[i]==ima:
            print(name[i])
            index=i
    if index=="no":
            print("not found")
    else:
                print(f"temperament:{temperament[index]}")
                webbrowser.open(image[index])

def goal(mission):
     print("What is the purpose of getting the dog")
     mission=input("what will the dog be doing ")
     for i in range(len(name)):
          if mission in bredfor[i]:
               print(f"name:{name[i]}")

def home(page):
     print("where would you like to go pound,tone, or goal")
     where=input("where are you going")
     if where=="pound":
          pound("tiny")
     elif where=="tone":
          tone("aloof")
     else:
          goal("hunting")




#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en













#main

