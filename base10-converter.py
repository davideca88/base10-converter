'''
PT-BR:
    Algoritmo para conversão da base decimal para uma base B "qualquer" (o código está limitado a base máxima 36 por falta de digitos. Se deseja aumentar a base máxima, adicione mais símbolos na lista "digits")
    Código de exemplo para o trabalho 1 da matéria de Experiência Criativa no curso de Ciência da Computação

EN:
    Algorithm to converte an decimal base number to an "any" B base (the code is limited to an 36 max base due to lack of digits. If you want to raise de max base, add more symbols in the "digits" list)
    Example code for "trabalho 1" (homework assignment no 1) of my Computer Science degree Creative Experience subject 
'''

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = int(input('Number to be converted (in decimal): '))
base = int(input('Base of which the number will be converted (int): '))

def converter(number: int, base: int) -> str:
    if base > len(digits):
        return f'Max supported base is {len(digits)} due to digits limits in this code. Consider add more symbols in the "digits" list.'

    if number == 0:
        return ''
    
    quotient = number // base
    module = number % base
    
    return converter(quotient, base) + digits[module]

print(converter(number, base))
