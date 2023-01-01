# Главное окно
from prettytable import PrettyTable
import tkinter as tk
import csv_creater
import data_base


def dis_add_contact(): # Метод включение добаление контактов
   lbl['text']= f'Введите Имя'
   btn6['state'] = tk.NORMAL    # разблокровка кнопки ок

def add_cont(x): # Метод добавление контакта
    global count
    global name
    global family
    global number
    if x ==1:
        count+=1
        name = ent.get()
        name = name.capitalize()
        lbl['text']= f'Введите Фамилию'
        ent.delete(0,tk.END)
    elif x ==2:
        count+=1
        family = ent.get()
        family = family.capitalize()
        lbl['text']= f'Введите Номер'
        ent.delete(0,tk.END)
    elif x ==3:
        count+=1
        number = int(ent.get())
        lbl['text']=f'Выберите действие'
        btn6['state'] = tk.DISABLED # блокировка кнопки
        csv_creater.name_csv(name)
        csv_creater.family_csv(family)
        csv_creater.number_csv(number)
        csv_creater.time_csv()
        data_base.write_base(name,family,number)
        ent.delete(0,tk.END)

        count = 1    

def read():  # Метод вывода 
    mytable = PrettyTable()
    mytable.field_names = ["Имя", "Фамилия", "Телефон"]
    temp = data_base.read_base()
    for i in temp:
        j = i.split()
        mytable.add_rows([j])
    lb_print['text'] = f'{mytable}'

def search_phon_book():  # Метод поиска
    sought = ent.get()
    if sought:
        sought = sought.lower()
        mytable = PrettyTable()
        mytable.field_names = ["Имя", "Фамилия", "Телефон"]
        temp = data_base.read_base()
        for i in temp:
            temp1 = i.split()
            for j in temp1:
                j = j.lower()
                if sought in j:
                    mytable.add_rows([temp1])
                lb_print['text'] = f'{mytable}'
    else:
        lb_print['text'] = f'Введите данные для поиска'  

def del_contact(): # Метод удаления контакта
    sought = ent.get()
    sought = sought.lower()
    mytable = PrettyTable()
    mytable.field_names = ["Имя", "Фамилия", "Телефон"]
    temp = data_base.read_base()
    for i in temp:
        temp1 = i.split()
        for j in temp1:
            if sought in j:
                temp.remove(temp1)
    for j in temp:
        fsn = j.split()
    data_base.remove_base(fsn[0],fsn[1],fsn[2])

count = 1

root = tk.Tk()

root.config(bg='#FFC400')  # Цвет фона окна в RGB или просто название на англиском  (rgb онлайн)
root.title('Телефоная книга')       #   Название окна
root.geometry("380x400+300+200")   #  Размер онка в пикселях и чурез + место вывода 

lbl = tk.Label(root,text=f'Выберите действие',font=('Arial', 12, 'bold'))
ent = tk.Entry(root,font=('Arial', 12, 'bold'))
lb_print = tk.Label(root) 

btn1 = tk.Button(font=('Arial', 10, 'bold'),text='Дабавить контакт',command=dis_add_contact)
btn2 = tk.Button(font=('Arial', 10, 'bold'),text='Вывод контактов',command=read)
btn3 = tk.Button(font=('Arial', 10, 'bold'),text='Поиск контакта',command=search_phon_book)
btn4 = tk.Button(font=('Arial', 10, 'bold'),text='Очистить лист', command=lambda:data_base.clear_base())
btn5 = tk.Button(font=('Arial', 10, 'bold'),text='Удалить контакт',command=del_contact)
btn6 = tk.Button(font=('Arial', 10, 'bold'),text='Ок',state='disabled', command=lambda:add_cont(count))

btn6.grid(row=0, column=2)

btn1.grid(row=2, column=0, stick='we')
btn2.grid(row=2, column=1, stick='we')
btn3.grid(row=2, column=2, stick='we')
btn4.grid(row=3, column=0, stick='we')
btn5.grid(row=3, column=1, stick='we')

lbl.grid(row=1,column=0,columnspan=3)
ent.grid(row=0,column=0,columnspan=2)
lb_print.grid(row=4,column=0,columnspan=3)

root.grid_columnconfigure(0,minsize=100) # минимальный размер 0 колонки
root.grid_columnconfigure(1,minsize=100) # минимальный размер 1 колонки
root.grid_columnconfigure(2,minsize=100) # минимальный размер 2 колонки

root.grid_rowconfigure(0,minsize=50) # минимальный размер 0 столбцов
root.grid_rowconfigure(1,minsize=50) # минимальный размер 0 столбцов



root.mainloop()    # конец