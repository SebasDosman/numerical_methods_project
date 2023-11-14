from math_functions import select_function
from menu_functions.helpers import clear_screen, display_main_menu
from numerical_methods import (riemann_sum_left, riemann_sum_middle,
                               riemann_sum_right, riemann_sum_trapezoidal,
                               riemann_sum_trapezoidal_full, romberg,
                               simpson_rule_one_eight,
                               simpson_rule_one_eight_composite,
                               simpson_rule_three_eight,
                               simpson_rule_three_eight_composite)


def integrals_menu() -> None:
    clear_screen()
    
    print('\n---------- Métodos de cálculo de integrales ----------\n')
    
    print('1. Sumas de Riemann por izquierda')
    print('2. Sumas de Riemann por el medio')
    print('3. Sumas de Riemann por derecha')
    print('4. Sumas de Riemann con trapecios')
    print('5. Sumas de Riemann con trapecios completa')
    print('6. Regla de Simpson 1/8')
    print('7. Regla de Simpson 1/8 compuesta')
    print('8. Regla de Simpson 3/8')
    print('9. Regla de Simpson 3/8 compuesta')
    print('10. Método de Romberg')
    print('11. Volver al menú principal')
    
    choice = input('\nSeleccione una opción: ')
    
    if choice == '1':
        print('\n---------- Sumas de Riemann por izquierda ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            riemann_sum_left(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '2':
        print('\n---------- Sumas de Riemann por el medio ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            riemann_sum_middle(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
            
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '3':
        print('\n---------- Sumas de Riemann por derecha ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            riemann_sum_right(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '4':
        print('\n---------- Sumas de Riemann con trapecios ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            riemann_sum_trapezoidal(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '5':
        print('\n---------- Sumas de Riemann con trapecios completa ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            riemann_sum_trapezoidal_full(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '6':
        print('\n---------- Regla de Simpson 1/8 ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n')
        
        try:
            simpson_rule_one_eight(a, b, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '7':
        print('\n---------- Regla de Simpson 1/8 compuesta ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            simpson_rule_one_eight_composite(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '8':
        print('\n---------- Regla de Simpson 3/8 ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            simpson_rule_three_eight(a, b, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '9':
        print('\n---------- Regla de Simpson 3/8 compuesta ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n---- Ingrese el valor de n ----\n')
        n = int(input('n = '))
        
        print('\n')
        
        try:
            simpson_rule_three_eight_composite(a, b, n, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '10':
        print('\n---------- Regla de Simpson 3/8 compuesta ----------\n')
        
        f = select_function()
        
        print('\n---- Ingrese el valor de a ----\n')
        a = int(input('a = '))
        
        print('\n---- Ingrese el valor de b ----\n')
        b = int(input('b = '))
        
        print('\n')
        
        try:
            romberg(a, b, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '11':
        input('\nVolviendo al menú principal. Pulse cualquier tecla...')
        display_main_menu()
    else:
        print('\n¡Opción inválida! Por favor ingrese otra opción')