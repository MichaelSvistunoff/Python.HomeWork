import mod_functions as fn
from mod_detalization import detalization_data

# Словарь меню
menu_dict = {
    "Добавление данных": fn.add,
    "Просмотр данных": fn.show, 
    "Удаление данных": fn.delete,  
    "Редактировать данные": fn.edit_data,
    "Показать деталезацию маршрута": detalization_data, 
    "Добавить маршрут": fn.add,
    "Завершить программу": fn.exit_,
}

# Пункты меню
menu_list = [
    "Добавление данных",
    "Просмотр данных",
    "Удаление данных",
    "Редактировать данные",
    "Показать деталезацию маршрута",
    "Добавить маршрут",
    "Завершить программу",
]
    
# Маршрутный справочник
def menu():
    fn.clear_screen()
    print('Маршрутный справочник\n')
    for index, option in enumerate(menu_list):
        print(f"{index+1} - {option}")
    input_ = input('\nВыбрать действие(введите индекс): ')
    while input_ not in ('1', '2', '3', '4', '5', '6', '7'):
        print('Пожалуйста, выберите 1, 2, 3, 4, 5, 6 или 7')
        input_ = input('Выберите действие(введите индекс): ')
    index_choose = int(input_[0])
    function = menu_dict[menu_list[index_choose-1]]
    function()