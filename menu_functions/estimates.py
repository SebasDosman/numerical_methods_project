from math_functions import select_function
from menu_functions.helpers import clear_screen, display_main_menu
from numerical_methods import (newton_interpolation, display_lagrange_interpolation, 
                               display_linear_regression_simple, display_linear_regression_multiple)


def estimates_menu() -> None:
    clear_screen()
    
    print('\n---------- Métodos de cálculo de estimaciones ----------\n')
    
    print('1. Método de interpolación de Newton')
    print('2. Método de interpolación de Lagrange')
    print('3. Método de regresión lineal simple')
    print('4. Método de regresión lineal múltiple')
    print('5. Volver al menú principal')
    
    choice = input('\nSeleccione una opción: ')
    
    if choice == '1':
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n---- Ingrese el valor de x ----\n')
        x = int(input('x = '))
        
        print('\n')
        
        try:
            newton_interpolation(a, b, n, f, x)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '2':
        print('\n---------- Método de interpolación de Lagrange ----------\n')
        
        print('\n')
        
        try:
            display_lagrange_interpolation()
        except Exception as e:
            print('\nError: {}'.format(e))
            
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '3':
        print('\n---------- Método de regresión lineal simple ----------\n')
        
        print('\n')
        
        try:
            display_linear_regression_simple()
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '4':
        print('\n---------- Método de regresión lineal múltiple ----------\n')
        
        print('\n')
        
        try:
            display_linear_regression_multiple()
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '5':
        input('\nVolviendo al menú principal. Pulse cualquier tecla...')
        display_main_menu()
    else:
        print('\n¡Opción inválida! Por favor ingrese otra opción')