import tkinter as tk
import Kartochka as ka

Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R  lern und Spaß...')
Bild = tk.PhotoImage(file='Phoenixx.png')
Okno.iconphoto(False, Bild)
Okno.geometry("800x615+300+120")
Okno.resizable(False, False)

frame_Head = tk.Frame(Okno, width=620, height=100)
frame_Body = tk.Frame(Okno, width=670, height=379)
frame_Footer = tk.Frame(Okno, width=620, height=50)
frame_Button = tk.Frame(Okno, width=620, height=40)

frame_Head.pack_propagate(False)
frame_Head.pack(side='top', fill='x')
frame_Body.pack_propagate(False)
frame_Body.pack(fill='x')
frame_Button.pack_propagate(False)
frame_Button.pack(side='bottom', fill='x')
frame_Footer.pack_propagate(False)
frame_Footer.pack(side='bottom', fill='x')

tk.Label(frame_Head, text=' D  o  c  t  o  r  ,  m e i n e   e r s t e   A p p... ', bg="#66B2FF", fg="#FFFFFF",
         width=50, font=('times', 20, 'bold')).pack(pady=10)
tk.Label(frame_Body,
         text='Приветствую и добро пожаловать!\n Для продолжения выберите одну из \nкатегории представленных ниже или '
              'в пунктах меню\n\n . . . \n---------------------------------\n---------------------------',
         font=('times', 20, 'bold')).pack(pady=50)
tk.Button(frame_Button, text='Экономка', activebackground='#938FA6', activeforeground='#5F837F', fg='#B7BCD0',
          bg='#5F837F', width=11, font=('times', 20, 'bold'), command=lambda: ka.ekonomka()).grid(row=0, column=0,
                                                                                                  padx=7)
tk.Button(frame_Button, text='Карточки', activebackground='#FFFFFF', activeforeground='#66B2FF', width=11, bg='#66B2FF',
          fg='#FFFFFF', font=('times', 20, 'bold'), command=lambda: ka.kartohk()).grid(row=0, column=1, padx=6)
tk.Button(frame_Button, text='Источник', activebackground='#5EB8C0', activeforeground='#D2F06A', bg='#D2F06A',
          fg='#5EB8C0', width=11, font=('times', 20, 'bold'), command=lambda: ka.qule()).grid(row=0, column=2, padx=6)
tk.Button(frame_Button, text='Викторина', activebackground='#000000', activeforeground='#EDD154', bg="#EDD154",
          fg="#000000", width=11, font=('times', 20, 'bold'), command=lambda: ka.wiktorina()).grid(row=0, column=3,
                                                                                                   padx=7)

main_menu = tk.Menu()
main_menu.add_cascade(label='Викторина', command=lambda: ka.wiktorina())
main_menu.add_cascade(label='Карточки', command=lambda: ka.kartohk())
main_menu.add_cascade(label='Экономка', command=lambda: ka.ekonomka())
main_menu.add_cascade(label='Источник', command=lambda: ka.qule())

Okno.config(menu=main_menu)
Okno.mainloop()
