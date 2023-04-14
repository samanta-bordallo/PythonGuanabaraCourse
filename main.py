# Functions
def hello():
    print("Hello, world")


def interact():
    name = input("What is your name?")
    print(f"Hello, {name}, nice to meet you")

def somatoria():
    number1 = int(input("Give me a number "))
    number2 = int(input("Give me another number"))
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

def new_word():
    word = input("Digite algo: ")
    print(f"O tipo primitivo desse valor é {type(word)}")
    print(f"Só tem espaços? {str.isspace(word)}")
    print(f"É um número? {str.isdigit(word)}")
    print(f"É alfabético? {str.isalpha(word)}")
    print(f"Está em maiúsculas? {str.isupper(word)}")
    print(f"Está em minusculas? {str.islower(word)}")
    print(f"Está capitalizada? {str.istitle(word)}")

def suc_ant():
    number = int(input('Diga um número '))
    print(f'O antecessor de {number} é {number - 1} e o sucessor é {number + 1}')

def dobro():
    number2 = int(input('Diga um número '))
    print(f'o dobro de {number2} é {number2 * 2}, o triplo é {number2 * 3} e a raiz quadrada é {number2 ** (1/2)}')

def media_notas():
    nota1 = int(input("Qual a primeira nota? "))
    nota2 = int(input("Qual a sugunda nota? "))
    print(f'A média da nota é {(nota1 + nota2) / 2}')

def metros():
    metros = int(input("Me de um número"))
    print(f'Então teremos para {metros} metro(s): {metros * 100} centímetros e {metros * 1000} milímetros')

def tabuada():
    numero_tabuada = 0
    number_tabuada = int(input("Me de um número "))
    print(f'A tabuada desse número é: \n')
    while numero_tabuada < 10:
        numero_tabuada += 1
        print(f" {number_tabuada} * {numero_tabuada} = {number_tabuada * numero_tabuada}")

def carteira():
        quantia_dinheiro = float(input("Quantos reais você têm? "))
        print(f'Esse valor de {quantia_dinheiro:.2f} R$ dá para comprar {quantia_dinheiro / 3.27:.2f} US$')

# Menus
def menu_world1():
    while True:
        print("\nselect a function to run:")
        print("1. Hello")
        print("2. your name")
        print("3. Math...")
        print("4. One word")
        print("5. Qual o antecessor")
        print("6. dobro")
        print("7. Media notas")
        print("8. metros")
        print("9. tabuada")
        print('10. carteira')
        print("0. quit")

        world1_input = input("\nEnter your choice: ")

        if world1_input == "1":
            hello()

        elif world1_input == "2":
            interact()

        elif world1_input == "3":
            somatoria()

        elif world1_input == "4":
            new_word()

        elif world1_input == "5":
            suc_ant()

        elif world1_input == "6":
            dobro()

        elif world1_input == "7":
            media_notas()

        elif world1_input == "8":
            metros()

        elif world1_input == "9":
            tabuada()

        elif world1_input == "10":
            carteira()

        elif world1_input == "0":
            print("Goodbye")
            break

        else:
            print("You cannot do this, try again")


# Main
def main():
    menu_world1()


if __name__ == "__main__":
    main()
