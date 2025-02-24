# COMO ENTENDER E RESOLVER ERROS?

# Exemplo de Stacktrace de erro:
# Divisão por 0, exemplo: 1/0 (não é possível dividir por zero)
# Erro de sintaxe no código, exemplo: print("Olá) (faltou fechar aspas)
# Identação incorreta, exemplo: print("Oi") (sem espaço antes de um bloco "if") 
# Variável não definida, exemplo: print(nome) (sem definir nome antes)
# Tipo de dado incompatível, exemplo: 3 + "a" (não pode somar número cm string)
# Índice fora do intervalo em listas/tuplas, exemplo: lista[10] (em uma lista que tem apenas 5 itens)
# Chave inexistente em um dicionário, exemplo: dados["idade"], (dados["idade"], mas idade não existe no dicionário)
# Valor incompatível com a operação, exemplo int("abc") (tentando converter string para inteiro)


# DICA: CONFERIR NO STACK OVERFLOW 

# Operadores de comparação em Python 

# == (igual a), exemplo: 5 == 5
# != (Diferente de) exemplo: 5!= 3
# > (Maior que) exemplo: 10 > 5
# < (Menor que) exemplo: 3 < 7
# >= (Maior ou igual a) 
# <= (Menor ou igual a)

#numeros = [10, 20, 30]
#indice = int(input("Digite um índice para acessar a lista: "))
#try:
#    print(numeros[indice])
#except:
#    print("Numero muito alto")
    
    
#def dividir(a, b):
#    try: (a / b)
#    except: b == 0
   

#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")
#try:
#    resultado = dividir(int(num1), int(num2))
#    print(f"Resultado: {resultado}")
#except ValueError:
#    print("Erro, número inválido")

# dados = {
#    "nome": "Isaac ",
#    "idade": 25,
#    "cidade": "São Paulo"
#}

#chave = input("Digite a chave que deseja acessar: ")
#try:
 #   print(f"O valor da chave '{chave}' é: {dados[chave]}")
#except KeyError:
#    print("Chave não existente")

#while True:
#    def validar_idade(idade):
#        if idade < 0 or idade > 120:
#            raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
#        return f"Idade válida: {idade}"
#    try:
#        idade = int(input("Digite sua idade: "))
#        print(validar_idade(idade))
#    except ValueError:
#        print("Insira um valor válido")

def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade
for i in range(0,4):
    try:
        notas = (input("Digite suas notas: "))
    except ValueError:
        print("Insira uma nota válida")
media = calcular_media(notas)
print(f"Média: {media:.2f}")