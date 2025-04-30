import math
from colorama import Fore, Style, init
import locale

init(autoreset=True)

# Define o locale para português do Brasil (Windows-friendly)
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR')
except locale.Error:
    locale.setlocale(locale.LC_ALL, '')

def formatar_numero(num):
    return locale.format_string('%.2f', num, grouping=True).replace('.', '#').replace(',', '.').replace('#', ',')

def parse_numero(valor):
    return float(valor.replace('.', '').replace(',', '.'))

def exibir_menu():
    print(Fore.CYAN + "\n=== CALCULADORA CIENTÍFICA ===")
    print(Fore.YELLOW + "Operações disponíveis:")
    print(Fore.GREEN + "  +   -> Soma")
    print("  -   -> Subtração")
    print("  *   -> Multiplicação")
    print("  /   -> Divisão")
    print("  ^   -> Potência")
    print("  √   -> Raiz quadrada")
    print("  sen -> Seno (em graus)")
    print("  cos -> Cosseno (em graus)")
    print("  tan -> Tangente (em graus)")
    print("  %   -> Porcentagem:")
    print("         - Ex: '20 % de 150'  → Digite: % de")
    print("         - Ex: '150 + 20%'    → Digite: +%")
    print("         - Ex: '150 - 20%'    → Digite: -%")
    print(Fore.MAGENTA + "Digite 'sair' para encerrar\n")

def calcular_unario(operacao, num):
    match operacao:
        case '√':
            return math.sqrt(num)
        case 'sen':
            return math.sin(math.radians(num))
        case 'cos':
            return math.cos(math.radians(num))
        case 'tan':
            return math.tan(math.radians(num))

def calcular_binario(operacao, num1, num2):
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '^':
            return num1 ** num2

def calcular_porcentagem():
    tipo = input("Digite o tipo de operação (% de / +% / -%): ").strip()
    
    if tipo == "% de":
        p = parse_numero(input("Digite a porcentagem (ex: 20): "))
        valor = parse_numero(input("Digite o valor base (ex: 150): "))
        resultado = valor * (p / 100)
    elif tipo == "+%":
        valor = parse_numero(input("Digite o valor base: "))
        p = parse_numero(input("Digite a porcentagem a adicionar: "))
        resultado = valor + (valor * (p / 100))
    elif tipo == "-%":
        valor = parse_numero(input("Digite o valor base: "))
        p = parse_numero(input("Digite a porcentagem a subtrair: "))
        resultado = valor - (valor * (p / 100))
    else:
        print(Fore.RED + "Tipo de porcentagem inválido!")
        return

    print(Fore.GREEN + f"Resultado: {formatar_numero(resultado)}")

def calculadora():
    operacoes_unarias = {'√', 'sen', 'cos', 'tan'}
    operacoes_binarias = {'+', '-', '*', '/', '^'}

    while True:
        exibir_menu()
        op = input(Fore.CYAN + "Escolha a operação: ").strip().lower()

        if op == 'sair':
            print(Fore.LIGHTBLUE_EX + "Encerrando a calculadora. Até a próxima!")
            break

        try:
            if op == '%':
                calcular_porcentagem()
            elif op in operacoes_unarias:
                num = parse_numero(input("Digite o número: "))
                resultado = calcular_unario(op, num)
                print(Fore.GREEN + f"Resultado: {formatar_numero(resultado)}")
            elif op in operacoes_binarias:
                num1 = parse_numero(input("Digite o primeiro número: "))
                num2 = parse_numero(input("Digite o segundo número: "))
                resultado = calcular_binario(op, num1, num2)
                print(Fore.GREEN + f"Resultado: {formatar_numero(resultado)}")
            else:
                print(Fore.RED + "Operação inválida!")
        except ZeroDivisionError:
            print(Fore.RED + "Erro: Divisão por zero!")
        except ValueError:
            print(Fore.RED + "Erro: Entrada inválida, digite apenas números.")
        except Exception as e:
            print(Fore.RED + f"Erro inesperado: {e}")

# Agora exibimos o menu assim que o programa inicia
exibir_menu()
calculadora()
