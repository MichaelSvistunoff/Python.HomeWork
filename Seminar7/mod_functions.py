import os
import sys
import mod_menu as m

# Добавить автобус / водителя / рейс
def add():
    clear_screen()
    print("Вы находитесь в режиме добавления (1 - автобус, 2 - водитель, 3 - маршрут, Enter - выход):\n")
    selection = input('Введите команду: ')
    match selection:
        case '1':   # Добавление автобуса
            bus_id      = "empty"
            bus_name    = "empty"
            bus_num     = "empty"
            bus_color   = "empty"
            while bus_name and bus_num and bus_color:
                bus_name = input('\nМарка автобуса: ').title()
                if not bus_name:
                    break
                bus_num = input('Номер автобуса: ').upper()
                if not bus_num:
                    break
                bus_color = input('Цвет автобуса: ').upper()
                if not bus_color:
                    break
                with open('list-buses.txt', 'a', encoding='utf8') as database:
                    bus_id = F"BUS-{id(bus_name)}"
                    data = f"{bus_id},{bus_name},{bus_num },{bus_color}\n"
                    database.write(data)
                print(f"Автобус '{bus_name}' добавлен в список!\n")
            m.menu()
        case '2':   # Добавление водителя
            driver_id       = "empty"
            driver_name     = "empty"
            driver_surname  = "empty"
            driver_exp      = "empty"
            while driver_name and driver_surname and driver_exp:
                driver_name = input('\nИмя водителя: ').title()
                if not driver_name:
                    break
                driver_surname = input('Фамилия водителя: ').title()
                if not driver_surname:
                    break
                driver_exp = input('Стаж вождения, лет: ')
                if not driver_exp:
                    break
                with open('list-drivers.txt', 'a', encoding='utf8') as database:
                    driver_id  = F"DRIVER-{id(driver_name)}"
                    data = f"{driver_id },{driver_name},{driver_surname},{driver_exp}\n"
                    database.write(data)
                print(f"Водитель '{driver_name}' добавлен в список!\n")
            m.menu()
        case '3':   # Добавление маршрута
            rout_id     = "empty"
            rout_name   = "empty"
            point_a     = "empty"
            point_b     = "empty"
            bus_id      = "empty"
            driver_id   = "empty"
            while rout_name and bus_id and driver_id and point_a and point_b:                
                rout_name = input('\nНомер маршрута: ').title()
                if not rout_name:
                    break       
                point_a = input('Введите начало маршрута: ').upper()
                if not point_a:
                    break
                point_b = input('Введите конец маршрута: ').upper()
                if not point_b:
                    break
                
                print('Выберите марку автобуса из списка: ')
                # Вывод списка для просмотра и выдора индекса
                with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                    new_list    = ''
                    if data_buses:
                        for idx, bus in enumerate(data_buses, start=0):
                            if bus:
                                bus = bus.strip().split(",")
                                new_list += f"{idx} - {bus[1]}\n"
                    else:
                        print('Пока нет автобусов!')
                    print('\n' + new_list) 
                bus_id = input('Введите индекс марки автобуса: ')
                if not bus_id:
                    return m.menu()
                with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                    lines = data_buses.readlines()
                    for bus in lines:
                        if bus == lines[int(bus_id)]:
                            result = bus.strip().split(",")[0]
                bus_id = result 
                
                print('Выберите водителя из списка: ')
                # Вывод списка для просмотра и выдора индекса
                with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                    new_list    = ''
                    if data_drivers:
                        for idx, driver in enumerate(data_drivers, start=0):
                            if driver:
                                driver = driver.strip().split(",")
                                new_list += f"{idx} - {driver[1]} {driver[2]}\n"
                    else:
                        print('Пока нет водителей!')
                    print('\n' + new_list) 
                driver_id = input('Введите индекс водителя: ')
                if not driver_id:
                    return m.menu()
                with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                    lines = data_drivers.readlines()
                    for driver in lines:
                        if driver == lines[int(driver_id)]:
                            result = driver.strip().split(",")[0]
                driver_id = result 
                with open('list-routes.txt', 'a', encoding='utf8') as database:
                    rout_id = F"ROUT-{id(rout_name)}"
                    data = f"{rout_id},{rout_name},{point_a},{point_b},{bus_id},{driver_id}\n"
                    database.write(data)
                print(f"Маршрут '{rout_name}' добавлен в список!\n")
            m.menu()
        case _:     # Неверная выборка
            return m.menu()

# Показать автобус / водителя / рейс
def show():
    clear_screen()
    print("Вы находитесь в режиме просмотра (1 - автобус, 2 - водитель, 3 - маршрут, Enter - выход):\n")
    selection = input('Введите команду: ')
    print()
    match selection:
        case '1':   # Просмотр автобуса
            with open('list-buses.txt', 'r', encoding='utf8') as database:
                lines = database.readlines()
                count = 0
                if lines:
                    for line in lines:
                        if line:
                            line = line.strip().split(",")
                            print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
                            count += 1
                    print(f"\nВ справочнике найдено автобусов: {count}")
                else:
                    print('Пока нету автобусов!')
            input('\nНажмите Enter, чтобы вернуться в меню')
            m.menu()
        case '2':   # Просмотр водителя
            with open('list-drivers.txt', 'r', encoding='utf8') as database:
                lines = database.readlines()
                count = 0
                if lines:
                    for line in lines:
                        if line:
                            line = line.strip().split(",")
                            print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
                            count += 1
                    print(f"\nВ справочнике найдено водителей: {count}")
                else:
                    print('Пока нету водителей!')
            input('\nНажмите Enter, чтобы вернуться в меню')
            m.menu()
        case '3':   # Просмотр маршрута
            with open('list-routes.txt', 'r', encoding='utf8') as database:
                lines = database.readlines()
                count = 0
                if lines:
                    for line in lines:
                        if line:
                            line = line.strip().split(",")
                            print(f"{line[0]},{line[1]},{line[2]},{line[3]},{line[4]},{line[5]}")
                            count += 1
                    print(f"\nВ справочнике найдено маршрутов: {count}")
                else:
                    print('Пока нету маршрутов!')
            input('\nНажмите Enter, чтобы вернуться в меню')
            m.menu()
        case _:     # Неверная выборка
            return m.menu()
 
# Удалить автобус / водителя / рейс
def delete():
    clear_screen()
    print("Вы находитесь в режиме удаления (1 - автобус, 2 - водитель, 3 - маршрут, Enter - выход):\n")
    selection = input('Введите команду: ')
    match selection:
        case '1':   # Удаление автобуса
            print('Удаление автобуса (для выхода нажмите Enter):')
            with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                new_data    = ''
                if data_buses:
                    for idx, bus in enumerate(data_buses, start=0):
                        if bus:
                            bus = bus.strip().split(",")
                            new_data += '{} - {}, {}\n'.format(idx, bus[1], bus[2] )
                else:
                    print('Пока нет автобусов!')
                print('\n' + new_data)   
            bus_name = "empty"
            while bus_name:
                bus_name = input('Введите индекс автобуса для удаления: ')
                if not bus_name:
                    break
                find = False
                with open('list-buses.txt', 'r', encoding='utf8') as buses_data:
                    buses = buses_data.readlines()
                    new_data = ''
                    for bus in buses:
                        if bus == buses[int(bus_name)]:
                            find = True                            
                            bus = bus.strip().split(",")
                            print('Автобус {} был удален\n'.format(bus[1]))
                            continue
                        new_data += bus
                with open('list-buses.txt', 'w', encoding='utf8') as buses_data:
                    buses_data.write(new_data)
                if not find:
                    print('Автобус не найден')
            m.menu()
        case '2':   # Удаление водителя
            print('Удаление водителя (для выхода нажмите Enter):')
            with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                new_data = ''
                if data_drivers:
                    for idx, driver in enumerate(data_drivers, start=0):
                        if driver:
                            driver = driver.strip().split(",")
                            new_data += '{} - {} {}\n'.format(idx, driver[1], driver[2])
                else:
                    print('Пока нет автобусов!')
                print('\n' + new_data)   
            driver_name = "empty"
            while driver_name:
                driver_name = input('Введите индекс водителя для удаления: ')
                if not driver_name:
                    break
                find = False
                with open('list-drivers.txt', 'r', encoding='utf8') as drivers_data:
                    drivers = drivers_data.readlines()
                    new_data = ''
                    for driver in drivers:
                        if driver == drivers[int(driver_name)]:
                            find = True                            
                            driver = driver.strip().split(",")
                            print('водитель {} был удален\n'.format(driver[1]))
                            continue
                        new_data += driver
                with open('list-drivers.txt', 'w', encoding='utf8') as drivers_data:
                    drivers_data.write(new_data)
                if not find:
                    print('Водитель не найден!')
            m.menu()
        case '3':   # Удаление маршрута
            print('Удаление водителя (для выхода нажмите Enter):')
            with open('list-routes.txt', 'r', encoding='utf8') as data_routs:
                new_data = ''
                if data_routs:
                    for idx, rout in enumerate(data_routs, start=0):
                        if rout:
                            rout = rout.strip().split(",")
                            new_data += '{} - Маршрут № {}: {}-{}\n'.format(idx, rout[1], rout[2], rout[3])
                else:
                    print('Пока нет маршрутов!')
                print('\n' + new_data)   
            rout_name = "empty"
            while rout_name:
                rout_name = input('Введите индекс маршрута для удаления: ')
                if not rout_name:
                    break
                find = False
                with open('list-routes.txt', 'r', encoding='utf8') as routs_data:
                    routs = routs_data.readlines()
                    new_data = ''
                    for rout in routs:
                        if rout == routs[int(rout_name)]:
                            find = True                            
                            rout = rout.strip().split(",")
                            print('Маршрут № {}: {}-{} был удален\n'.format(rout[1], rout[2], rout[3]))
                            continue
                        new_data += rout
                with open('list-routes.txt', 'w', encoding='utf8') as routes_data:
                    routes_data.write(new_data)
                if not find:
                    print('Маршрут не найден')
            m.menu()
            return m.menu()
        case   _:   # Неверная выборка
            return m.menu()
        
# Изменить данные автобуса / водителя / рейса
def edit_data():
    clear_screen()
    print("Вы находитесь в режиме редактирования (1 - автобус, 2 - водитель, 3 - маршрут, Enter - выход):\n")
    selection = input('Введите команду: ')
    match selection:
        case '1':   # Редактирование автобуса
            with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                new_data    = ''
                if data_buses:
                    for idx, bus in enumerate(data_buses, start=0):
                        if bus:
                            bus = bus.strip().split(",")
                            new_data += f"{idx} - {bus[2]}\n"
                else:
                    print('Пока нет автобусов!')
                print('\n' + new_data)            
            input_ = "empty"
            while input_:
                input_ = input("Введите индекс автобуса для редактирования: (Enter - выход в меню): ")
                if not input_:
                    break
                find = False
                with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                    lines = data_buses.readlines()
                    new_data = ''
                    new_mark = "empty"
                    new_id_number = "empty"
                    new_color = "empty"
                    for bus in lines:
                        if bus != lines[int(input_)]:
                            new_data += bus
                        else:
                            find = True
                            # У автобуса следющие поля:
                            # [0]-id,[1]-Марка,[2]-Номер,[3]-Цвет
                            bus = bus.strip().split(",")
                            print('\nМарка: {}\nГос. номер: {}\nЦвет: {}\n'.format(bus[1], bus[2],bus[3]))
                            print('Вы можете изменить: 1 - Марка, 2 - Гос. номер, 3 - Цвет (Enter - выход в меню) ')
                            selection = input('Введите команду для редактирования: ')
                            if not selection:
                                return m.menu()
                            match selection:
                                case '1':   # bus[1] - Меняем марку автобуса 
                                    print('Смена марки автобуса ({}): '.format(bus[1]))
                                    new_mark = input('Введите новую марку: ').upper()
                                    if not new_mark:
                                        return m.menu()                                      
                                    bus[1] = new_mark
                                    bus = '{},{},{},{}\n'.format(bus[0], bus[1], bus[2], bus[3])
                                    print('Марка автобуса успешно отредактирована!')
                                case '2':   # bus[2] - Меняем номер автобуса 
                                    print('Смена гос. номера автобуса ({}): '.format(bus[2]))
                                    new_id_number = input('Введите новый гос. номер: ').upper()
                                    if not new_id_number:
                                        return m.menu()
                                    bus[2] = new_id_number
                                    bus = '{},{},{},{}\n'.format(bus[0], bus[1], bus[2], bus[3])
                                    print('Гос. номер автобуса успешно отредактирована!') 
                                case '3':   # bus[3] - Меняем цвет автобуса 
                                    print('Смена цвета автобуса ({}): '.format(bus[3]))
                                    new_color = input('Введите новый цвет: ').upper()
                                    if not new_color:
                                        return m.menu()
                                    bus[3] = new_color
                                    bus = '{},{},{},{}\n'.format(bus[0], bus[1], bus[2], bus[3])
                                    print('Цвет автобуса успешно отредактирована!')  
                                case _:
                                    break
                            new_data += bus
                            pass
                with open('list-buses.txt', 'w', encoding='utf8') as data_buses:
                    data_buses.writelines(new_data)                  
                if not find:
                    print("Такой автобус не найден!")
            m.menu()
        case '2':   # Редактирование водителя
            with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                new_data    = ''
                if data_drivers:
                    for idx, driver in enumerate(data_drivers, start=0):
                        if driver:
                            driver = driver.strip().split(",")
                            new_data += f"{idx} - {driver[2]}\n"
                else:
                    print('Пока нет водителей!')
                print('\n' + new_data)            
            input_ = "empty"
            while input_:
                input_ = input("Введите индекс водителя для редактирования: (Enter - выход в меню): ")
                if not input_:
                    break
                find = False
                with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                    lines = data_drivers.readlines()
                    new_data = ''
                    new_name = "empty"
                    new_surname = "empty"
                    new_experience = "empty"
                    for driver in lines:
                        if driver != lines[int(input_)]:
                            new_data += driver
                        else:
                            find = True
                            # У водителя следющие поля:
                            # [0]-id,[1]-Имя,[2]-Фамилия,[3]-Стаж
                            driver = driver.strip().split(",")
                            print('\nИмя: {}\nФамилия: {}\nСтаж: {}\n'.format(driver[1], driver[2],driver[3]))
                            print('Вы можете изменить: 1 - Имя, 2 - Фамилию, 3 - Стаж (Enter - выход в меню) ')
                            selection = input('Введите команду для редактирования: ')
                            if not selection:
                                return m.menu()
                            match selection:
                                case '1':   # driver[1] - Меняем имя водителя
                                    print('Смена имени водителя ({}): '.format(driver[1]))
                                    new_name = input('Введите новую марку: ').title()
                                    if not new_name:
                                        return m.menu()                                      
                                    driver[1] = new_name
                                    driver = '{},{},{},{}\n'.format(driver[0], driver[1], driver[2], driver[3])
                                    print('Имя водителя успешно отредактирована!')
                                case '2':   # driver[2] - Меняем фамилию водителя
                                    print('Смена фамилии водителя ({}): '.format(driver[2]))
                                    new_surname = input('Введите новую фамилию: ').title()
                                    if not new_surname:
                                        return m.menu()
                                    driver[2] = new_surname
                                    driver = '{},{},{},{}\n'.format(driver[0], driver[1], driver[2], driver[3])
                                    print('Фамилия водителя успешно отредактирована!') 
                                case '3':   # driver[3] - Меняем стаж 
                                    print('Изменение стажа вождения водителя ({}): '.format(driver[3]))
                                    new_experience = input('Введите стаж: ').upper()
                                    if not new_experience:
                                        return m.menu()
                                    driver[3] = new_experience
                                    driver = '{},{},{},{}\n'.format(driver[0], driver[1], driver[2], driver[3])
                                    print('Стаж вождения водителя успешно отредактирован!')  
                                case _:
                                    break
                            new_data += driver
                            pass
                with open('list-drivers.txt', 'w', encoding='utf8') as data_drivers:
                    data_drivers.writelines(new_data)                  
                if not find:
                    print("Такой водитель не найден!")
            m.menu()
        case '3':   # Редактирование маршрута
            with open('list-routes.txt', 'r', encoding='utf8') as data_routs:
                new_data    = ''
                if data_routs:
                    for idx, rout in enumerate(data_routs, start=0):
                        if rout:
                            rout = rout.strip().split(",")
                            new_data += f"{idx} - {rout[2]}\n"
                else:
                    print('Пока нет маршрутов!')
                print('\n' + new_data)            
            input_ = "empty"
            while input_:
                input_ = input("Введите индекс маршрута для редактирования: (Enter - выход в меню): ")
                if not input_:
                    break
                find = False
                with open('list-routes.txt', 'r', encoding='utf8') as data_routs:
                    lines = data_routs.readlines()
                    new_data = ''
                    for rout in lines:
                        if rout != lines[int(input_)]:
                            new_data += rout
                        else:
                            find = True
                            rout = rout.strip().split(",")
                            print('\nНомер маршрута: {}\nНачальная остановка: {}\nКонечная остановка: {}\nАвтобус: {}\nВодитель: {}'\
                                .format(rout[1], rout[2], rout[3], rout[4], rout[5]))
                            print('\nВы можете изменить: 1 - Номер маршрута, 2 - Начальную остановку, 3 - Конечную остановку, 4 - Автобус, 5 - Водителя (Enter - выход в меню) ')
                            selection = input('Введите команду для редактирования: ')
                            if not selection:
                                return m.menu()
                            match selection:
                                case '1':   # rout[1] - Меняем номер маршрута
                                    print('Смена номера маршрута ({}): '.format(rout[1]))
                                    new_rout = input('Введите новый номер маршрута: ').title()
                                    if not new_rout:
                                        return m.menu()                                      
                                    rout[1] = new_rout
                                    rout = '{},{},{},{},{},{}\n'.format(rout[0], rout[1], rout[2], rout[3], rout[4], rout[5])
                                    print('Номер маршрута успешно отредактирован!')
                                case '2':   # rout[2] - Меняем начальную остановку
                                    print('Смена начальной остановки ({}): '.format(rout[2]))
                                    new_point_a = input('Введите новую начальную остановку: ').upper()
                                    if not new_point_a:
                                        return m.menu()
                                    rout[2] = new_point_a
                                    rout = '{},{},{},{},{},{}\n'.format(rout[0], rout[1], rout[2], rout[3], rout[4], rout[5])
                                    print('Начальная остановка успешно отредактирована!') 
                                case '3':   # rout[3] - Меняем конечную остановку
                                    print('Смена начальной остановки ({}): '.format(rout[3]))
                                    new_point_b = input('Введите новую конечную остановку: ').upper()
                                    if not new_point_b:
                                        return m.menu()
                                    rout[3] = new_point_b
                                    rout = '{},{},{},{},{},{}\n'.format(rout[0], rout[1], rout[2], rout[3], rout[4], rout[5])
                                    print('Конечная остановка успешно отредактирована!') 
                                case '4':   # rout[4] - Меняем автобус
                                    print('Смена автобуса ({}): '.format(rout[4]))
                                    result = "empty"
                                    # Вывод списка для просмотра и выдора индекса
                                    with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                                        new_list    = ''
                                        if data_buses:
                                            for idx, bus in enumerate(data_buses, start=0):
                                                if bus:
                                                    bus = bus.strip().split(",")
                                                    new_list += f"{idx} - {bus[1]}\n"
                                        else:
                                            print('Пока нет автобусов!')
                                        print('\n' + new_list) 
                                    new_selection = input('Введите индекс нового автобуса из списка: ')
                                    if not new_selection:
                                        return m.menu()
                                    with open('list-buses.txt', 'r', encoding='utf8') as data_buses:
                                        lines = data_buses.readlines()
                                        for bus in lines:
                                            if bus == lines[int(new_selection)]:
                                                result = bus.strip().split(",")[0]
                                    rout[4] = result                                                   
                                    rout = '{},{},{},{},{},{}\n'.format(rout[0], rout[1], rout[2], rout[3], rout[4], rout[5])
                                    print('Автобус успешно отредактирован!')
                                case '5':   # rout[5] - Меняем водителя
                                    print('Смена водителя ({}): '.format(rout[5]))
                                    result = "empty"
                                    # Вывод списка для просмотра и выдора индекса
                                    with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                                        new_list    = ''
                                        if data_drivers:
                                            for idx, driver in enumerate(data_drivers, start=0):
                                                if driver:
                                                    driver = driver.strip().split(",")
                                                    new_list += f"{idx} - {driver[1]}\n"
                                        else:
                                            print('Пока нет автобусов!')
                                        print('\n' + new_list) 
                                    new_selection = input('Введите индекс нового водителя из списка: ')
                                    if not new_selection:
                                        return m.menu()
                                    with open('list-drivers.txt', 'r', encoding='utf8') as data_drivers:
                                        lines = data_drivers.readlines()
                                        for driver in lines:
                                            if driver == lines[int(new_selection)]:
                                                result = driver.strip().split(",")[0]
                                    rout[5] = result                                                   
                                    rout = '{},{},{},{},{},{}\n'.format(rout[0], rout[1], rout[2], rout[3], rout[4], rout[5])
                                    print('Водитель успешно отредактирован!')
                                case _:
                                    break
                            new_data += rout
                            pass
                with open('list-routes.txt', 'w', encoding='utf8') as data_routs:
                    data_routs.writelines(new_data)                  
                if not find:
                    print("Такой маршрут не найден!")
            m.menu()
        case _:     # Неверная выборка
            return m.menu()

# Выйти из приложения
def exit_():
    clear_screen()
    sys.exit()

# Очистить экран
def clear_screen():
    os.system("cls")