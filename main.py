from menu_functions.main import main_menu


if __name__ == '__main__':
    try:
        main_menu()
    except Exception as e:
        print('\nError: {}'.format(e))