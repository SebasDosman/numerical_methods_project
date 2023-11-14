from math_functions import select_function
from menu_functions.helpers import (calculate_gx, clear_screen,
                                    display_main_menu, find_roots,
                                    graphic_function)
from numerical_methods import (bisection, false_position, fixed_point,
                               newton_raphson, newton_raphson_multiple, secant)


def select_range(numerical_method : callable) -> None:
    clear_screen()
    
    print('\n---------- ¿Desea trabajar con intervalos ó relizarlo automáticamente? ----------\n')
    
    print('1. Si, deseo trabajar con intervalos')
    print('2. No, deseo que se realice automáticamente')
    
    choice = input('\nSeleccione una opción: ')
    
    if choice == '1':
        print('\n---- Ingrese el intervalo para hallar la raíz de la función ----\n')
        
        f = select_function()
        
        graphic_function(f)
        
        a = float(input('\nIntervalo a = '))
        b = float(input('Intervalo b = '))
        print('\n')

        try:
            numerical_method(a, b, f)
        except Exception as e:
            print("\nError: {}".format(e))
            
    elif choice == '2':
        print('\n---- Ingrese la cantidad de intervalos a utilizar ----\n')
        
        cant_range = int(input('Cantidad de intervalos = '))
        print('\n')
        
        find_roots(numerical_method, cant_range)
    else:
        print('\n¡Opción inválida! Por favor ingrese otra opción\n')


def roots_menu() -> None:
    clear_screen()
    
    print('\n---------- Métodos de busqueda de raíces ----------\n')
    
    print('1. Método de punto fijo')
    print('2. Método de bisección')
    print('3. Método de la falsa posición')
    print('4. Método de Newton-Raphson')
    print('5. Método de la secante')
    print('6. Método de Newton-Raphson para raíces multiples')
    print('8. Volver al menú principal')
    
    choice = input('\nSeleccione una opción: ')
    
    if choice == '1':
        print('\n---------- Método de punto fijo ----------\n')
        
        f = select_function()
        
        graphic_function(f)
        
        print('\n---- Ingrese el valor de x ----\n')
        x = float(input('x = '))
        print('\n')
        
        g = calculate_gx(f, x)
        
        try:
            fixed_point(x, g)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '2':
        print('\n---------- Método de bisección ----------\n')
        
        try:
            select_range(bisection)
        except Exception as e:
            print('\nError: {}'.format(e))
            
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '3':
        print('\n---------- Método de la falsa posición ----------\n')
        
        try:
            select_range(false_position)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '4':
        print('\n---------- Método de Newton-Raphson ----------\n')
        
        f = select_function()
        
        graphic_function(f)
        
        print('\n---- Ingrese el valor de x ----\n')
        x = float(input('x = '))
        print('\n')
        
        try:
            newton_raphson(x, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '5':
        print('\n---------- Método de la Secante ----------\n')
        
        try:
            select_range(secant)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '6':
        print('\n---------- Método de Newton Raphson para raices multiples ----------\n')
        
        f = select_function()
        
        graphic_function(f)
        
        print('\n---- Ingrese el valor de x ----\n')
        x = float(input('x = '))
        print('\n')
        
        try:
            newton_raphson_multiple(x, f)
        except Exception as e:
            print('\nError: {}'.format(e))
        
        input('\nPresione cualquier tecla para continuar...\n')
    elif choice == '8':
        input('\nVolviendo al menú principal. Pulse cualquier tecla...')
        display_main_menu()
    else:
        print('\n¡Opción inválida! Por favor ingrese otra opción\n')