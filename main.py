from Lists import LinkedOrderedList
from ABR import ABR
from ARN import ARN

def main():
    test = ARN()
    test.insertNewValue(20)
    n16 = test.insertNewValue(16)
    test.insertNewValue(28)
    n19 = test.insertNewValue(19)
    test.insertNewValue(7)
    test.display()
    x = test.OS_Select(1)
    if x is not None:
        print(x.value)
    print(test.OS_Rank(n16))
    print(test.OS_Rank(n19))
    return 0


if __name__ == '__main__':
    main()