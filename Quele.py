import Gui as gu
import webbrowser as wb


def display_title():
    gu.tk.Label(gu.frame_Head, text="  И  С  Т  О  Ч  Н  И  К  И  ",
                width=50, height=100, bg="#D2F06A", fg="#5EB8C0", font=('times', 20, 'bold')).pack()


class Quele:
    def __init__(self):
        display_title()
        gu.tk.Button(gu.frame_Body, text='Читать', width=20, bg="#D2F06A", fg="#5EB8C0",
                     font=('times', 20, 'bold'), command=self.chitat).pack(pady=15)
        gu.tk.Button(gu.frame_Body, text='Смотреть', width=20, bg="#D2F06A", fg="#5EB8C0",
                     font=('times', 20, 'bold'), command=self.smotret).pack(pady=15)
        gu.tk.Button(gu.frame_Body, text='Слушать', width=20, bg="#D2F06A", fg="#5EB8C0",
                     font=('times', 20, 'bold'), command=self.sluschat).pack(pady=15)
        gu.tk.Button(gu.frame_Body, text='Писать', width=20, bg="#D2F06A", fg="#5EB8C0",
                     font=('times', 20, 'bold'), command=self.pisat).pack(pady=15)
    def chitat(self):
        wb.open("https://deutsch.info/")

    def smotret(self):
        wb.open("https://www.youtube.com/channel/UCHpnIL-1QIUyVhdGVJ6rW3A")

    def sluschat(self):
        wb.open("https://audio-class.ru/deutsch/german-songs/Efimia-Zeit.php")

    def pisat(self):
        wb.open("https://www.de-online.ru/testy_i_uprazhneniya")
