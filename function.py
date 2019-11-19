def nested_functionI(arg1, arg2):

    def inner(word):
        var = word + '!!!'
        return var
    return inner('okay'), inner('good')

def nested_functionII(n):

    def inner(word):
        var = word * n
        return var
    
    return inner

def basic_function():
    var = 'Hello basic function'
    return var

def arg_function(arg1, arg2):
    var = str(arg1) + ' ' + str(arg2)
    return var 

def main():
    print(basic_function())

    first, second = nested_functionI('Hello', ' python !')
    print(first + ' ' + second)

    third = nested_functionII(3)
    print(third('Python '))
    
if __name__ == '__main__':
    main()