#zadnie 1
for i in range(1, 100):
    if(i % 15 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)

#zadnie 2
def numer_to_word(n):
    liczby = {'1' : "jeden",
              '2' : "dwa",
              '3' : "trzy",
              '4' : "cztery",
              '5' : "pięć",
              '6' : "sześć",
              '7' : "siedem",
              '8' : "osiem",
              '9' : "dziewięć",
              '0' : "zero"}
    for num in str(n):
        print(liczby[num], end=' ')

#zadnie 3
def arabic_to_roman():
    number = int(input('Podaj liczbe: '))
    
    num_in_roman = ''
    arabic_roman={1000: 'M',
                    900: 'CM',
                    500: 'D',
                    400: 'CD',
                    100: 'C',
                    90: 'XC',
                    50: 'L',
                    40: 'XL',
                    10: 'X',
                    9: 'IX',
                    5: 'V',
                    4: 'IV',
                    1: 'I'
                    }
    for arabic, roman in arabic_roman.items():
        num_in_roman += number // arabic * roman
        number %= arabic
    print(num_in_roman)
