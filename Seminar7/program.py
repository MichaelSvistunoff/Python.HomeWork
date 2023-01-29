from mod_menu import menu

if __name__ == "__main__":
    try:
        with open('list-buses.txt', 'x'):
            pass
        with open('list-drivers.txt', 'x'):
            pass
        with open('list-routes.txt', 'x'):
            pass
    except FileExistsError:
        pass
    menu()