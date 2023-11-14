from menu_functions.helpers import clear_screen, display_main_menu
from numerical_methods import (display_dominant_matrix, display_gauss,
                               display_jacobi)


def equation_systems_menu() -> None:
    clear_screen()
    
    print('\n---------- Métodos de cálculo de sistemas de ecuaciones ----------\n')
    
    print('1. Método de la matríz dominante')
    print('2. Método de Gauss')
    print('3. Método de Jacobi')
    print('4. Volver al menú principal')
    
    choice = input('\nSeleccione una opción: ')
    
    if choice == '1':
        print('\n---------- Método de la matríz dominante ----------\n')
        
        print('\n---- Ingrese el valor de la potencia p ----\n')
        p = int(input('p = '))
        
        print('\n---- Ingrese la cantidad de iteraciones i ----\n')
        i = int(input('i = '))
        
        print('\n')
        
        try:
            display_dominant_matrix(p, i)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '2':
        print('\n---------- Método de Gauss ----------\n')
        
        print('\n---- Ingrese el valor de la potencia p ----\n')
        p = int(input('p = '))
        
        print('\n---- Ingrese la cantidad de iteraciones i ----\n')
        i = int(input('i = '))
        
        print('\n')
        
        try:
            display_gauss(p, i)
        except Exception as e:
            print('\nError: {}'.format(e))
            
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '3':
        print('\n---------- Método de Jacobi ----------\n')
        
        print('\n---- Ingrese el valor de la potencia p ----\n')
        p = int(input('p = '))
        
        print('\n---- Ingrese la cantidad de iteraciones i ----\n')
        i = int(input('i = '))
        
        print('\n')
        
        try:
            display_jacobi(p, i)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '4':
        input('\nVolviendo al menú principal. Pulse cualquier tecla...')
        display_main_menu()
    else:
        print('\n¡Opción inválida! Por favor ingrese otra opción')