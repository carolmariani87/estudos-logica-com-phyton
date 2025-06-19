def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    print("Calculadora Básica")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    
    try:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        
        if operacao == '+':
            resultado = soma(a, b)
        elif operacao == '-':
            resultado = subtrai(a, b)
        elif operacao == '*':
            resultado = multiplica(a, b)
        elif operacao == '/':
            resultado = divide(a, b)
        else:
            print("Operação inválida.")
            return
        
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos.")

