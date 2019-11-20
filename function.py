def lambda_function1():
    x = lambda a, b: a ** b
    print(x(10, 2))

def lambda_map():
    animals = ["divisio", "ordo", "familia", "genus", "species"]

    new_animals = map(lambda item : item + '_', animals)

    print(list(new_animals))

def lambda_filter():
    animals = ["divisio", "ordo", "familia", "genus", "species"]

    new_animals = filter(lambda item : len(item) > 6, animals) 

    print(list(new_animals))

def lambda_function2():
    x = lambda word, counter : word * counter
    print(x('hello ', 6))

def kwlength_argument(**kwargs):
    for key, value in kwargs.items():
        print(key + ' : ' + value)

def length_argument(*args):
    var = ''

    for data in args:
        var += data + ' '
    return var

def default_argument(arg1, itterate = 10):
    #Open code below to reset itterate
    #itterate = 7
    var = (arg1 + ' ') * itterate
    return var

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

    print(default_argument('Hello'))

    print(length_argument("Hello", "python", "scripting"))
    
    kwlength_argument(name='Patrick', age='14', address='Bikini Bottom')

    lambda_function1()

    lambda_function2()

    lambda_map()

    lambda_filter()

if __name__ == '__main__':
    main()