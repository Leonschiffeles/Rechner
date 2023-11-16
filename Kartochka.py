import Gui as gu
import json
import random


def display_title():
    gu.tk.Label(gu.frame_Body, text=" K A R T O C H K I ", width=41, bg="grey", fg="red",
                font=('times', 20, 'bold')).pack(side='top')


class Carten:
    def __init__(self):
        self.vvod_sl()
        self.dobav_sl()
        self.dobav_zn()
        self.display_cartu = gu.tk.Label(gu.frame_Body, text=self.display_cartu, width=25, height=5, bg="#66B2FF",
                                         fg="#FFFFFF", font=('times', 30, 'bold')).pack(side='top')
        self.display_true()
        self.button_u = gu.tk.Button(gu.frame_Button, text="Udalit", width=20, height=2, bg="#66B2FF", fg="#FFFFFF",
                                     font=('times', 15, 'bold'))
        self.button_u["command"] = self.button_ud
        self.button_u.grid(row=0, column=0, padx=8, pady=3)
        self.button_d = gu.tk.Button(gu.frame_Button, text="Dalee", width=20, height=2, bg="#66B2FF", fg="#FFFFFF",
                                     font=('times', 15, 'bold'))
        self.button_d["command"] = self.button_da
        self.button_d.grid(row=0, column=1, padx=8, pady=3)
        self.button_do = gu.tk.Button(gu.frame_Button, text="Dobavit", width=20, height=2, bg="#66B2FF", fg="#FFFFFF",
                                      font=('times', 15, 'bold'))
        self.button_do["command"] = self.button_dob
        self.button_do.grid(row=0, column=2, padx=8, pady=3)

    def display_true(self):
        pass

    def button_da(self):
        pass

    def button_ud(self):
        with open('Kart.json', 'r', encoding="utf-8") as Card:
            data = json.load(Card)
            spis = 0
            for slow in data["Carts"]:
                if slow["slovo"] == self.vvod.get():
                    data['Carts'].pop(spis)
                spis += 1
            with open('Kart.json', 'w', encoding="utf-8") as wikhod:
                json.dump(data, wikhod, ensure_ascii=False, indent=1)

    def button_dob(self):
        dobavit = {self.dob_sl.get(): self.dob_zn.get()}
        with open('Kart.json', encoding="utf-8") as Card:
            data = json.load(Card)
            data['Carts'].append(dobavit)
            with open('Kart.json', 'w', encoding="utf-8") as Wukhod:
                json.dump(data, Wukhod, ensure_ascii=False, indent=1)

    def display_cartu(self):
        with open('Kart.json', 'r', encoding="utf-8") as Card:
            data = json.load(Card)
            random.choice(list(data.slovo()))

    def vvod_sl(self):
        self.vvod = gu.tk.Entry(gu.frame_Body, width=35, bg="#FFFFFF", fg="#66B2FF", justify="center",
                                font=('times', 20, 'bold')).pack(side='bottom', pady=8)

    def dobav_sl(self):
        self.dob_sl = gu.tk.Entry(gu.frame_Footer, width=27, bg="#FFFFFF", fg="#66B2FF", justify="center",
                                  font=('times', 20, 'bold')).pack(side="left")

    def dobav_zn(self):
        self.dob_zn = gu.tk.Entry(gu.frame_Footer, width=27, bg="#FFFFFF", fg="#66B2FF", justify="center",
                                  font=('times', 20, 'bold')).pack(side='right')
