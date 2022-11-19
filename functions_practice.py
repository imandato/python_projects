def hello():
    print("Hello user")

hello()

def pack(argument1, argument2, argument3):
    return [argument1, argument2, argument3]

print(pack("apples", "bananas", "pears"))

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I eat {lunch[0]}")
            else:
                print(f"Next I eat {lunch[i]}")
    

eat_lunch(["pears", "apples", "oranges"])
