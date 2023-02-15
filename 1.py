hasReservedWord = [
    'auto', 'break', 'case', 'char',
    'const','continue', 'default','do', 
    'double', 'else', 'enum', 'extern',
    'float', 'for', 'goto', 'if', 
    'int', 'long', 'register', 'return',
    'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union',
    'unsigned',	'void',	'volatile',	'while'] #palavras reservadas 

hasInteger = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #números inteiros
hasGeneral = ['+', '-', '*', '/', '%', '++', '--'] #operadores artmeticos, relacionas e caracteres especiais
lineContent = []
lineTokens = []

code = open('arquivoemc.txt', 'r')
content = code.readlines()

def compiler():
    for line in content:
        cleanContent = line.split(' ')
        for item in cleanContent:
            if(hasReservedWord._contains_(item)):
                print('TOKEN: Palavra reservada')
            if(hasInteger._contains_(item)):
                print('TOKEN: Número inteiro')

compiler()

'''
       
'''