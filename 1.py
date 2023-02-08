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
hasToken = ['+', '-', '*', '/', '%', '++', '--'] #operadores artmeticos, relacionas e caracteres especiais
lineContent = []
response = []

code = open('arquivoemc.txt', 'r')
content = code.readlines()

def compiler():
    for line in content:
        response.clear
        cleanContent = line.replace(' ', '')
        lineContent.a
        
       
        print(cleanContent)
    return

compiler()

'''
        if():
            response.__add__('Palavra reservada')
        if():
            response.__add__('Inteiro')
        if():
            response.__add__('Token')
'''