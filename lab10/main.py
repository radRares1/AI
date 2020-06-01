from cont import *


if __name__ == '__main__':
    
    #temp = int(input("input the temperature\n"))
    #cap = int(input("input the capacity\n"))
    
    print("first example\n")
    c1 = Controller(22,2)
    c1.solve()
    print("\nsecond example\n")
    c2 = Controller(50,6)
    c2.solve()