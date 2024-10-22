from Lists import LinkedOrderedList

def main():
    test = LinkedOrderedList()
    test.insertNewValue(20)
    test.insertNewValue(16)
    test.insertNewValue(28)
    n19 = test.insertNewValue(19)
    test.insertNewValue(7)
    test.display()
    if test.OS_Select(6) is not None:
        print(test.OS_Select(6).value)
    print(test.OS_Rank(n19))
    return 0


if __name__ == '__main__':
    main()