from menu_functions.helpers import clear_screen


def display_derivatives_menu() -> None:
    from menu_functions import derivatives_menu
    derivatives_menu()

def display_roots_menu() -> None:
    from menu_functions import roots_menu
    roots_menu()

def display_integrals_menu() -> None:
    from menu_functions import integrals_menu
    integrals_menu()

def display_equation_systems_menu() -> None:
    from menu_functions import equation_systems_menu
    equation_systems_menu()

def display_estimates_menu() -> None:
    from menu_functions import estimates_menu
    estimates_menu()

def main_menu() -> None:
    while True:
        clear_screen()
        
        print('\n---------- Bienvenido a Métodos Numéricos ----------\n')
        print('1. Derivadas')
        print('2. Métodos de busqueda de raíces')
        print('3. Métodos de cálculo de integrales')
        print('4. Métodos de cálculo de sistemas de ecuaciones')
        print('5. Métodos de cálculo de estimaciones')
        print('6. Salir')
        
        choice = input('\nSeleccione una opción: ')
        
        if choice == '1':
            display_derivatives_menu()
        elif choice == '2':
            display_roots_menu()
        elif choice == '3':
            display_integrals_menu()
        elif choice == '4':
            display_equation_systems_menu()
        elif choice == '5':
            display_estimates_menu()
        elif choice == '6':
            print('\n¡Hasta la próxima!')
            break
        else:
            print('\n¡Opción inválida! Por favor ingrese otra opción')