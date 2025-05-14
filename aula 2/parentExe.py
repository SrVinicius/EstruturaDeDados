# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    #------- COLOQUE SEU CÓDIGO AQUI -------
    pares = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # Professor, dei uma olhada nessa parte do in (python é no mínimo "estranho" kkkk)
        if char in '({[':
            pilha.push(char)
        elif char in ')}]':
            if pilha.is_empty() or pilha.pop() != pares[char]:
                return False

    return pilha.is_empty()


    #---------------------------------------


# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
