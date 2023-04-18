import pygame
import random
import math

pygame.init()


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
    print(f'o dobro de {number2} é {number2 * 2}, o triplo é {number2 * 3} e a raiz quadrada é {number2 ** (1 / 2)}')


def media_notas():
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a sugunda nota? "))
    print(f'A média da nota é {(nota1 + nota2) / 2}')


def metros():
    metros1 = float(input("Me de um número"))
    print(f'Então teremos para {metros1} metro(s): {metros1 * 100} centímetros e {metros1 * 1000} milímetros')


def tabuada():
    numero_tabuada = 0
    number_tabuada = int(input("Me de um número "))
    print(f'A tabuada desse número é: \n')
    while numero_tabuada < 10:
        numero_tabuada += 1
        print(f" {number_tabuada} x {numero_tabuada} = {number_tabuada * numero_tabuada}")


def carteira():
    quantia_dinheiro = float(input("Quantos reais você têm? "))
    print(f'Esse valor de {quantia_dinheiro:.2f} R$ dá para comprar {quantia_dinheiro / 3.27:.2f} US$')


def tintas():
    largura = float(input('Qual a largura da parede? '))
    altura = float(input('Qual a altura da parede? '))
    print(
        f'A área da sua parede é {largura * altura} m2, logo você vai precisar de '
        f'{(largura * altura) / 2} latas de tinta')


def desconto():
    preco = float(input("Qual o valor do produto? "))
    print(f"o novo valor do produto com 5% de desconto é: {preco * 0.95} R$")


def salario():
    salario1 = float(input('Qual o seu sálário? '))
    print(f"Seu salário aumentou em 15%. Você passará a receber {salario1 * 1.15} R$")


def graus():
    grau = float(input("What's the temperature?"))
    print(f"The temperature {grau}ªC corresponds to {grau * 1.8 + 32} ªF ")


def car():
    days = int(input("How many days was? "))
    km = float(input("How many kilometers was? "))
    print(f"You should pay {(days * 60) + (km * 0.15)} R$")


def real_number():
    number_real = float(input("Give me a number "))
    print(f"The number {number_real} has the integer part {math.floor(number_real)}")


def leg():
    opposite_leg = float(input("What is the length of the opposite leg? "))
    adjacent_leg = float(input("What is the length of the adjacent leg? "))
    print(f"The hypotenuse will be {math.sqrt((opposite_leg ** 2) + (adjacent_leg ** 2))} ")


def angle():
    angle1 = float(input("Give me a angle"))
    rad = math.radians(angle1)
    print(
        f"For this angle, we have {math.sin(rad):.2f} sine, {math.cos(rad):.2f} "
        f"cosine and {math.tan(rad):.2f} tangent")


def student():
    student1 = input("Writing the first name ")
    student2 = input("Writing the second name ")
    student3 = input("Writing the third name ")
    student4 = input("Writing the fourth name ")
    lista1 = [student1, student2, student3, student4]
    random_student = random.choice(lista1)
    print(f"The student choose was: {random_student}")


def students_presentation():
    student1 = input("Writing the first name ")
    student2 = input("Writing the second name ")
    student3 = input("Writing the third name ")
    student4 = input("Writing the fourth name ")
    lista1 = [student1, student2, student3, student4]
    random.shuffle(lista1)
    print(f"The order of presentation is: {lista1}")


def music():
    pygame.init()
    pygame.mixer.music.load("Fatality.mp3")

    # # loop principal do programa
    # while True:
    #     # verifica se alguma tecla foi pressionada
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             # verifica se a tecla "P" foi pressionada
    #             if event.key == K_RETURN:
    #                 # toca a música
    pygame.mixer.music.play()


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
        print('11. Tintas')
        print('12. Desconto')
        print('13. Salário')
        print("14. Graus")
        print("15. Car")
        print("16. Real Number")
        print("17. Legs")
        print("18. Angle")
        print("19. Random student")
        print("20. Student presentation")
        print("21. Music")
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

        elif world1_input == "11":
            tintas()

        elif world1_input == "12":
            desconto()

        elif world1_input == "13":
            salario()

        elif world1_input == "14":
            graus()

        elif world1_input == "15":
            car()

        elif world1_input == "16":
            real_number()

        elif world1_input == "17":
            leg()

        elif world1_input == "18":
            angle()

        elif world1_input == "19":
            student()

        elif world1_input == "20":
            students_presentation()

        elif world1_input == "21":
            music()

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
