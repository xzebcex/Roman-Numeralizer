# This application converts Integers to Roman Numbers.
# Roman_numeralizer.

# Seven different letters represent Roman numerals: I,V,X,L,C,D, and M.
# Which symbolise the numerals 1,5,10,50,100,500, and 1,000.
# Thousands of numbers may be generated using just seven letters.

int_to_roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD',
                500: 'D', 900: 'CM', 1000: ' M'}

integer = int(input('Enter a number: '))

# Descending integer equivalent of seven roman numberals.
print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

roman_numeral = ''

for x in print_order:
    if integer != 0:
        quotient = integer//x

        # if quotient is not zero output thhe roman equivalent.
        if quotient != 0:
            for y in range(quotient):
                # print(int_to_roman[x], end='')
                roman_numeral += int_to_roman[x]

        # update integer with remainder.
        integer %= x


# print the Roman numeral equivalent.
print(roman_numeral)
