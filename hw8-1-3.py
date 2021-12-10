#author:DMH 12/9/21

def temp(x):
    temp = 0
    temp = (int(x) -32) / 1.8
    return temp 




temp_1 = input("What is temp(f)")

print(temp(temp_1))