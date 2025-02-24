#>>> Desafio: Criar uma Calculadora com Classes  

#Você deve criar uma classe chamada Calculadora que permita realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão. A calculadora também deve ser capaz de armazenar o histórico das operações realizadas. 
#Requisitos:  

#Classe Calculadora:  
#Deve ter um atributo chamado historico, que será uma lista para armazenar as operações realizadas.
#Deve ter os seguintes métodos:
#- adicionar(a, b): Retorna a soma de a e b e registra a operação no histórico.
#- subtrair(a, b): Retorna a diferença entre a e b e registra a operação no histórico.
#- multiplicar(a, b): Retorna o produto de a e b e registra a operação no histórico.
# dividir(a, b): Retorna a divisão de a por b e registra a operação no histórico. Caso b seja zero, deve lançar uma exceção informando que a divisão por zero não é permitida.
#- mostrar_historico(): Exibe todas as operações realizadas na calculadora, incluindo os números envolvidos e o resultado.

class Calculadora:
    def soma(n1, n2):
        soma = n1 + n2
        return soma
        
    def subtração(n1, n2):
        subtração = n1 - n2
        return subtração
        
    def multiplicação(n1, n2):
        multiplicação = n1 * n2
        return multiplicação
    
    def divisão(n1, n2):
        if n2 == 0:
            return("Erro, divisão por zero")
        divisão = n1 / n2
        return divisão
        
print("Selecione sua operação")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Mostrar Histórico")
print("6. Limpar Histórico")
histórico = []

while True:
    escolha = input("Digite sua escolha (1/2/3/4/5/6): ")
    
    if escolha in ['1', '2', '3', '4', '5', '6']:
        if escolha == '5':
            print(histórico)
        elif escolha == '6': histórico.clear()
        else:
            num1 = float(input("Digite seu primeiro número: "))
            num2 = float(input("Digite seu segundo número: "))
                
            
            if escolha == '1':
                print(f"{num1} + {num2} = {Calculadora.soma(num1, num2)}")   
                histórico.append(Calculadora.soma(num1, num2))
            elif escolha == '2':
                print(f"{num1} - {num2} = {Calculadora.subtração(num1, num2)}")
                histórico.append(Calculadora.subtração(num1, num2))
                
            elif escolha == '3':
                print(f"{num1} * {num2} = {Calculadora.multiplicação(num1, num2)}")
                histórico.append(Calculadora.multiplicação(num1, num2))
                
            elif escolha == '4':
                print(f"{num1} / {num2} = {Calculadora.divisão(num1, num2)}")
                histórico.append(Calculadora.divisão(num1, num2))
    
    
    proxima_operação = input("Deseja realizar outra operação? (s/n): ")
    if proxima_operação.lower() != 's':
            break
         
    else:print("1. Soma  2. Subtração  3.Multiplicação  4.Divisão 5. Mostrar histórico 6.Limpar histórico")