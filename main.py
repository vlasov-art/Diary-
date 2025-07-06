from customtkinter import (
    # Основные классы
    CTk, CTkFrame, CTkCanvas,
    
    # Виджеты ввода
    CTkButton, CTkLabel, CTkEntry, CTkCheckBox, 
    CTkSwitch, CTkRadioButton, CTkProgressBar,
    CTkSlider, CTkOptionMenu, CTkComboBox, 
    CTkSegmentedButton, CTkTextbox, CTkScrollableFrame,
    
    # Специализированные виджеты
    CTkFont, CTkImage, CTkScrollbar, CTkTabview,
    
    # Диалоговые окна и сообщения
    CTkInputDialog,
    
    # Виджеты рисования
    CTkCanvas,
    
    # Системные настройки
    set_appearance_mode,  # "System", "Dark", "Light"
    set_default_color_theme,  # "blue", "green", "dark-blue", "yellow"
    get_appearance_mode,
    set_widget_scaling,  # Масштабирование виджетов
    set_window_scaling,   # Масштабирование окна
    
    # Константы
    CENTER, LEFT, RIGHT, TOP, BOTTOM, 
    BOTH, X, Y, HORIZONTAL, VERTICAL,
    NORMAL, DISABLED,
    SOLID, RAISED, SUNKEN, GROOVE, RIDGE,
    W, E, N, S, NS, EW, NSEW,
    
    # Стили
    ThemeManager
)
import tkinter as tk
import os
import sys
import shutil
import json

lessons = dict()

def resource_path(relative_path):
    """ Возвращает корректный путь для ресурсов """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def reg():
    app = CTk()
    app.title('Регистрация')
    app.geometry('1920x1080')
    set_appearance_mode('dark')
    app.iconbitmap('diary.ico')


    week = CTkTabview(app, height=800, width=1200, corner_radius=15)
    week.pack(padx=100, pady=100)


    label = CTkLabel(app, text=('Добавление вашего расписания'), text_color='white', font=("Arial", 24, "bold"))
    label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    week.add('Понедельник')
    week.add('Вторник')
    week.add('Среда')
    week.add('Четверг')
    week.add('Пятница')
    week.add('Суббота')


    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    def add_lesson(weekday):
        global lessons
        d1 = []
        for i in range(1, 9):
            d1.append(CTkEntry(week.tab(weekday), placeholder_text=str(i) + ' урок', corner_radius=10, width=650, height=40))
            d1[i - 1].place(relx=0.5, rely=0.05 + (i - 1) * 0.06, anchor=tk.CENTER)
        lessons[weekday] = d1


    def save_lessons():
        file = resource_path('lessons.txt')

        record_lessons = open(file, 'w', encoding='utf-8')

        for el in weekdays:
            record = ''
            for button in lessons[el]:
                record += button.get() + ' '
            print(record)
            print(record, file=record_lessons)
        record_lessons.close()

        


    for el in weekdays:
        add_lesson(el)

    button_save = CTkButton(master=app, text='Save', command=save_lessons)
    button_save.pack(padx=20, pady=10)

    app.mainloop()
    pass



def bas():
    app = CTk()
    app.title('Diary')
    app.geometry('1920x1080')
    set_appearance_mode('dark')
    set_default_color_theme('dark-blue')
    app.iconbitmap('diary.ico')


    menu = CTkTabview(app, height=1200, width=1600, corner_radius=20)
    menu.pack(padx=100, pady=100)


    menu.add('Настройки')
    menu.add('Home')
    menu.add('Расписание')
    menu.set('Home')

    #Расписание:

    timetable = CTkTabview(menu.tab('Расписание'), height=800, width=1200, corner_radius=20)
    timetable.add('Понедельник')
    timetable.add('Вторник')
    timetable.add('Среда')
    timetable.add('Четверг')
    timetable.add('Пятница')
    timetable.add('Суббота')

    timetable.pack()

    file = resource_path('lessons.txt')
    les = open(file, 'r', encoding='utf-8')

    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    matrix_btn = [[CTkButton(timetable.tab('Понедельник'))] * 8] * 8

    def homework(pair):

        home = CTk()
        home.title('Homework')
        home.geometry('1280x720')
        set_appearance_mode('dark')
        set_default_color_theme('dark-blue')
        home.iconbitmap('diary.ico')

        index1 = pair[0]
        index2 = pair[1]

        btn = matrix_btn[index1][index2]

        label = CTkLabel(home, text=('Добавление домашнего задания на ' + weekdays[index1]), text_color='white', font=("Arial", 24, "bold"))
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        add_homework = CTkEntry(home, placeholder_text='Добавить или заменить прошлое домашнее задание', width=300, height=30, corner_radius=20)
        add_homework.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        file = open('homework.json', 'r', encoding='utf-8')

        record_homework = json.load(file)

        homework_text = record_homework.get(str(index1) + str(index2), '')

        label_homework = CTkLabel(home, text=homework_text, text_color='white', font=("Arial", 20), width=300, height=30, corner_radius=20)
        label_homework.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        def save_homework():
            file = open('homework.json', 'w', encoding='utf-8')
            record_homework[str(index1) + str(index2)] = add_homework.get()
            json.dump(record_homework, file, ensure_ascii=False, indent=2)
            homework_text = record_homework.get(str(index1) + str(index2), '')

            label_homework = CTkLabel(home, text=homework_text, text_color='white', font=("Arial", 20), width=300, height=30, corner_radius=20)
            label_homework.place(relx=0.5, rely=0.3, anchor=tk.CENTER)



        save_home = CTkButton(home, text = 'Сохранить', width=300, height=30, corner_radius=20, command=save_homework)
        save_home.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        

        home.mainloop()



    for el in weekdays:
        lesson_day = les.readline().split()
        for urok in range(1, len(lesson_day) + 1):
            matrix_btn[weekdays.index(el)][urok - 1] = CTkButton(timetable.tab(el), width=300, height=60, corner_radius=20,
                                                                text=str(urok) + ' урок: ' + lesson_day[urok - 1],
                                                                text_color='white', font=("Arial", 20),
                                                                command=lambda idx=[weekdays.index(el), urok - 1]: homework(idx))
            matrix_btn[weekdays.index(el)][urok - 1].place(relx=0.5, rely=0.05 + (urok - 1) * 0.1, anchor=tk.CENTER)
        label = CTkLabel(timetable.tab(el), text='Нажмите на кнопку для добавление домашнего задания или для просмотра д/з этого дня', text_color='white', font=("Arial", 24, "bold"))
        label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


    app.mainloop()


file = resource_path('registry.txt')

registry = open(file, 'r+', encoding='utf-8')
if registry.read() == '0':
    registry.close()
    registry = open(file, 'w', encoding='utf-8')
    print('1', file=registry)
    reg()
    bas()
else:
    bas()