import tkinter as tk
import Kartochka as ka
import Woprosu as wp
import Ekonomka as ek
import Quele as qu

Okno = tk.Tk()
Okno.config(bg='#DADADA')
Okno.title('D O C T O R  lern und Spaß...')
Bild = tk.PhotoImage(file='Phoenixx.png')
Okno.iconphoto(False, Bild)
Okno.geometry("800x615+300+120")
Okno.resizable(False, False)

frame_Head = tk.Frame(Okno, width=620, height=100, bg='grey')
frame_Body = tk.Frame(Okno, width=670, height=379, bg='red')
frame_Footer = tk.Frame(Okno, width=620, height=50, bg='#FFFFFF')
frame_Button = tk.Frame(Okno, width=620, height=40, bg='#008FCD')

frame_Head.pack(side='top', fill='x')
frame_Body.pack(fill='x')
frame_Button.pack(side='bottom', fill='x')
frame_Footer.pack(side='bottom', fill='x')


def clear_Head():
    for widget in frame_Head.winfo_children():
        widget.destroy()


def clear_Body():
    for widget in frame_Body.winfo_children():
        widget.destroy()


def clear_Button():
    for widget in frame_Button.winfo_children():
        widget.destroy()


def clear_Footer():
    for widget in frame_Footer.winfo_children():
        widget.destroy()


def wiktorina():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    wp.Wiktorin()


def kartohka():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    ka.Carten()


def ekonomka():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    ek.ekonomka()


def qule():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    qu.qule()


main_menu = tk.Menu()
main_menu.add_cascade(label="Викторина", command=lambda: wiktorina())
main_menu.add_cascade(label="Карточки", command=lambda: kartohka())
main_menu.add_cascade(label="Экономка", command=lambda: ekonomka())
main_menu.add_cascade(label="Источник", command=lambda: qule())

Okno.config(menu=main_menu)
Okno.mainloop()
