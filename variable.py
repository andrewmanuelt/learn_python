def enum_word(var): #enumerate word
    word = var * 2
    return word

def global_var(): #global variable
    global int_var
    int_var = 10

def casting_var(str_var): #casting data int -> str
    echo = 'Hello ' + str_var + ' ' + str(int_var)
    return echo

def main():
    global_var()
    print(enum_word('hoola ! '))
    print(casting_var('Ahmad'))

if __name__ == '__main__':
    main()

