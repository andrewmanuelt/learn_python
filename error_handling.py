def error_handling():
    x = 10

    try:
        print(len(x))
    except:
        print('Unable to get length of int')

    return x

def raise_if():
    x = 9

    if x < 10:
        raise ValueError('X must be greater than 10')

    return x
    
def main():
    error_handling()
    raise_if()

if __name__ == '__main__':
    main()