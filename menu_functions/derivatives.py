from derivative_methods import (back_difference, center_difference, derivate,
                                front_difference, second_back_difference,
                                second_center_difference, second_derivate,
                                second_front_difference)
from math_functions import select_function
from menu_functions.helpers import clear_screen, display_main_menu


def derivatives_menu() -> None:
    clear_screen()
    
    print('\n---------- Derivadas ----------\n')
    print('1. Primera derivada de una función')
    print('2. Segunda derivada de una función')
    print('3. Derivada como diferencias fínitas')
    print('4. Volver al menú principal')
    
    choice = input('\nSeleccione una opción: ')
    
    if choice == '1':
        first_derivative()
    elif choice == '2':
        second_derivative()
    elif choice == '3':
        finite_derivatives()
    elif choice == '4':
        input('\nVolviendo al menú principal. Pulse cualquier tecla...')
        
        display_main_menu()
    else:
        input('\n¡Opción inválida! Pulse cualquier tecla...')

def first_derivative() -> None:
    clear_screen()
    
    print('\n---------- 1° Derivada de una función ----------\n')
    
    f = select_function()
    print('\n---- Ingrese el valor de x ----\n')
    
    x = int(input('x = '))
    print('\n1° Derivada de la función = {}'.format(derivate(x, f)))
    
    input('\nPresiona cualquier tecla para continuar...\n')

def second_derivative() -> None:
    clear_screen()
    
    print('\n---------- 2° Derivada de una función ----------\n')
    
    f = select_function()
    print('\n---- Ingrese el valor de x ----\n')
    
    x = int(input('x = '))
    print('\n2° Derivada de la función = {}'.format(second_derivate(x, f)))
    
    input('\nPresiona cualquier tecla para continuar...\n')

def finite_derivatives() -> None:
    clear_screen()
    
    print('\n---------- Derivadas como Diferencias Finitas ----------\n')
    f = select_function()
    print('\n---- Ingrese el valor de x y h ----\n')
    x = float(input('x = '))
    h = float(input('h = '))
    
    try:
        print('\nPrimera derivada central        = {}'.format(center_difference(x, h, f)))
        print('Segunda derivada central        = {}'.format(second_center_difference(x, h, f)))
        print('\nPrimera derivada a la izquierda = {}'.format(back_difference(x, h, f)))
        print('Segunda derivada a la izquierda = {}'.format(second_back_difference(x, h, f)))
        print('\nPrimera derivada a la derecha   = {}'.format(front_difference(x, h, f)))
        print('Segunda derivada a la derecha   = {}'.format(second_front_difference(x, h, f)))
    except Exception as e:
        print("\nError: {}".format(e))
        
    input('\nPresione cualquier tecla para continuar...\n')