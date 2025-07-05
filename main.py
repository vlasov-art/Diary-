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
    set_default_color_theme,  # "blue", "green", "dark-blue"
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



    week = CTkTabview(app, height=800, width=1200, corner_radius=15)
    week.pack(padx=100, pady=100)


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

        record_lessons = open(file, 'a')

        for el in weekdays:
            record = ''
            for button in lessons[el]:
                record += button.get() + ' '
            print(record, file=record_lessons)
        record_lessons.close()



    for el in weekdays:
        add_lesson(el)

    button_save = CTkButton(master=app, text='Save', command=save_lessons)
    button_save.pack(padx=20, pady=10)

    app.mainloop()
    pass




file = resource_path('registry.txt')

registry = open(file, 'r+')
if registry.read() == '0':
    reg()
else:
    pass