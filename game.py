#ibk
#function

def key():
    lv=input("do you want to play easy,medium, or hard mode")
    if lv==("hard"):
        for i in range(5):
                lock=input("enter in a number in the range of 1-100: ")
                if lock==("60"):
                    break
                if lock=="57" or "58" or "59" or "61" or "62" or "63":
                    print("hot")
                if lock=="55" or "56" or "64" or "65":
                    print("warm")
                if lock<("55"):
                    print("cold")
                if lock>("65"):
                    print("cold")
                print("wrong try again")
                if lock==("60"):
                    print("you win")

    elif lv ==("medium"):
        for i in range(5):
                open=input("enter in a number in the range of 1-50: ")
                if open==("11"):
                    break
                elif open=="8" or "9" or "10" or "12" or "13" or "14":
                    print("hot")
                elif open=="6" or "7" or "15" or "16":
                    print("warm")
                elif open<("6"):
                    print("cold")
                elif open>("14"):
                    print("cold")
                    print("wrong try again")
                elif open==("11"):
                    print("you win")
    else:
        for i in range(5):
                gate=input("enter in a number in the range of 1-1000: ")
                if gate==("531"):
                    break
                elif gate=="532" or "533" or "534" or "528" or "529" or "530":
                    print("hot")
                elif gate=="526" or "527" or "535" or "536":
                    print("warm")
                elif gate<("526"):
                    print("cold")
                elif gate>("536"):
                    print("cold")
                    print("wrong try again")
                elif gate==("531"):
                    print("you win")





#main
key()
