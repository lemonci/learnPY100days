def max2(x: list):
    if len(x)<2:
        print("There are less than 2 elements in the list")
        pass
    else:
        y = x[:]
        a = max(y)
        y.remove(a)
        b = max(y)
        return a, b

if __name__ == '__main__':
    max2([3,2,1])