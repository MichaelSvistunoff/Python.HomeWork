import mod_menu as m
from mod_functions import clear_screen
from random import randint

# Детализация рейса
def detalization_data():
    clear_screen()    
    rout_id             = "empty"
    rout_name           = "empty"
    rout_point_a        = "empty"
    rout_point_b        = "empty" 
    rout_bus_id         = "empty" 
    rout_driver_id      = "empty"
    rout_distance       = "empty"
    rout_stop_points    = "empty"
    rout_mid_speed      = "empty"
    rout_mid_clients    = "empty"
    rout_revenue        = "empty"
    ticket_cost         = 30
    bus_name            = "empty" 
    bus_number          = "empty" 
    bus_color           = "empty"
    driver_name         = "empty" 
    driver_surname      = "empty" 
    driver_exp          = "empty"
    find = False     
    print("Вы находитесь в режиме просмотра детализации\n")
    new_data = ''    
    with open('list-routes.txt', 'r', encoding='utf8') as database:
        if database:
            for idx, line in enumerate(database, start=0):
                if line:
                    line = line.strip().split(",")
                    new_data += '{} - Маршрут № {}: {}-{}\n'.format(idx, line[1], line[2], line[3])
        else:
            print('Пока нету маршрутов!')
        print(new_data)
    print('Выберите маршрут для детального просмотра (Enter - выход): ')
    input_ = "empty"
    while input_:  
        input_ = input('Введите индекс маршрута: ')
        if not input_:
            return m.menu()        
        find = False
        with open('list-routes.txt', 'r', encoding='utf8') as routs:                
            rout_lines = routs.readlines()                
            for rout in rout_lines:
                if rout == rout_lines[int(input_)]:                    
                    rout = rout.strip().split(",")
                    find                = True
                    rout_id             = rout[0]
                    rout_point_a        = rout[2]
                    rout_point_b        = rout[3]
                    rout_name           = rout[1]
                    rout_bus_id         = rout[4]
                    rout_driver_id      = rout[5]
                    rout_distance       = randint(30, 50)
                    rout_stop_points    = randint(15, 32)
                    rout_mid_speed      = randint(40, 70)
                    rout_mid_clients    = randint(800, 950)
                    rout_revenue        = rout_mid_clients * ticket_cost
                    pass
        if not find:
            print('Такой маршрут не найден!')
        find = False                
        with open('list-buses.txt', 'r', encoding='utf8') as buses:
            buses_lines = buses.readlines()
            for bus in buses_lines:
                bus = bus.strip().split(",")
                if rout_bus_id in bus[0]:                                
                    find = True
                    bus_name = bus[1]
                    bus_number = bus[2]
                    bus_color = bus[3]
                    pass
        if not find:
            print('Нет информации про автобус!')
        find = False
        with open('list-drivers.txt', 'r', encoding='utf8') as drivers:                
            drivers_lines = drivers.readlines()
            for driver in drivers_lines:
                driver = driver.strip().split(",")
                if rout_driver_id in driver[0]:                                
                    find = True
                    driver_name = driver[1]
                    driver_surname = driver[2]
                    driver_exp = driver[3]
                    pass
        if not find:
            print('Нет информации про водителя!')
        
        text =  '\nПолная информация по рейсу [{}]:\n'.format(rout_id)
        text += '----------------------------------\n'
        text += '  Информация по маршруту на рейсе:\n'
        text += '       № маршрута: {}\n'.format(rout_name)
        text += '       Направление маршрута: {}-{}\n'.format(rout_point_a, rout_point_b)
        text += '       Дистанция маршрута, км: {}\n'.format(rout_distance)
        text += '       Количество остановок на маршруте, шт: {}\n'.format(rout_stop_points)
        text += '       Среднее количество человек за день, чел: {}\n'.format(rout_mid_clients)
        text += '       Выручка за день, руб.: {}\n'.format(rout_revenue)
        text += '       Средняя скорость на маршруте, км/ч: {}\n'.format(rout_mid_speed)
        text += '  Информация по автобусу на рейсе:\n'
        text += '       Марка автобуса: {}\n'.format(bus_name)
        text += '       Регистрационный номер: {}\n'.format(bus_number)
        text += '       Цвет автобуса: {}\n'.format(bus_color.title())
        text += '   Информация по водителю на рейсе:\n'
        text += '       Фамилия водителя: {}\n'.format(driver_surname)
        text += '       Имя водителя: {}\n'.format(driver_name)
        text += '       Стаж водителя, лет: {}'.format(driver_exp)
        print(text)
        input('\nНажмите Enter, чтобы вернуться в меню')
        return m.menu()