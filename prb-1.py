# Solve me first usage

def solveMeFirst(a, b):
    if a >= 1 and a <= 1000:
        print("valid value for " + str(a))
    else:
        print("invalid value " + str(a) + "value is not in expected range")
    if b >= 1 and b <= 1000:
        print("valid value for " + str(b))
    else:
        print("invalid value " + str(b) + "value is not in expected range")
    res = (int(a) + int(b))
    print(res)


solveMeFirst(2, 3)


## Solution presented and accepted by Hacker Rank Community
def solvemefirst(a, b):
    return a + b


num_1 = int(input())
num_2 = int(input())
res = solvemefirst(num_1, num_2)
print(res)
