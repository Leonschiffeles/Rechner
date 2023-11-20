import Gui as gu
import json
import random


def display_title():
    gu.tk.Label(gu.frame_Head, text="  К   А   Р   Т   О   Ч   К   И  ",
                width=50, height=100, bg="#66B2FF", fg="#FFFFFF", font=('times', 20, 'bold')).pack()


class Carten:
    def __init__(self):
        self.tru = None
        display_title()
        self.cartu = gu.tk.StringVar()
        self.znach = gu.tk.StringVar()
        self.dob_sl = gu.tk.Entry(gu.frame_Footer, width=27, bg="#FFFFFF", fg="#66B2FF", justify="center",
                                  font=('times', 20, 'bold'))
        self.dob_sl.pack(side="left")

        self.dob_zn = gu.tk.Entry(gu.frame_Footer, width=27, bg="#FFFFFF", fg="#66B2FF", justify="center",
                                  font=('times', 20, 'bold'))
        self.dob_zn.pack(side='right')

        gu.tk.Label(gu.frame_Body, textvariable=self.cartu, width=15, height=3, bg="#66B2FF",
                    fg="#FFFFFF", font=('times', 50, 'bold')).pack(side='top', pady=15)

        gu.tk.Button(gu.frame_Body, text="Показывать значение", width=20, height=1, fg="#66B2FF", bg="#FFFFFF",
                     font=('times', 18, 'bold'), command=self.display_true).pack(side='left', anchor='sw', 
                                                                                 padx=5, pady=4)
        gu.tk.Button(gu.frame_Body, text="Cкрыть значение", width=20, height=1, fg="#66B2FF", bg="#FFFFFF",
                     font=('times', 18, 'bold'), command=self.skrut_true).pack(side='right', anchor='se', padx=5, 
                                                                               pady=4)

        self.button_u = gu.tk.Button(gu.frame_Button, text="Udalit", width=20, height=2, activebackground="#FFFFFF",
                                     activeforeground="#66B2FF", bg="#66B2FF", fg="#FFFFFF",
                                     font=('times', 15, 'bold'))
        self.button_u["command"] = self.button_ud
        self.button_u.grid(row=0, column=0, padx=8, pady=3)
        self.button_d = gu.tk.Button(gu.frame_Button, text="Dalee", width=20, height=2, activebackground="#FFFFFF",
                                     activeforeground="#66B2FF", bg="#66B2FF", fg="#FFFFFF",
                                     font=('times', 15, 'bold'))
        self.button_d["command"] = self.display_cartu
        self.button_d.grid(row=0, column=1, padx=8, pady=3)
        self.button_do = gu.tk.Button(gu.frame_Button, text="Dobavit", width=20, height=2, activebackground="#FFFFFF",
                                      activeforeground="#66B2FF", bg="#66B2FF", fg="#FFFFFF",
                                      font=('times', 15, 'bold'))
        self.button_do["command"] = self.button_dob
        self.button_do.grid(row=0, column=2, padx=8, pady=3)

    def display_true(self):
        self.tru = gu.tk.Label(gu.frame_Body, textvariable=self.znach, width=25, height=1, bg="#66B2FF",
                               fg="#FFFFFF", font=('times', 20, 'bold'))
        self.tru.pack(pady=2)

    def skrut_true(self):
        self.tru.pack_forget()

    def button_ud(self):
        slovo = self.dob_sl.get()
        znach = self.dob_zn.get()

        with open('Kart.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for cart in data["Carts"]:
            if cart["slovo"] == slovo and cart["znach"] == znach:
                data["Carts"].remove(cart)
                break

        with open('Kart.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def button_dob(self):
        new_slovo = self.dob_sl.get()
        new_znach = self.dob_zn.get()

        with open('Kart.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        new_kart = {"slovo": new_slovo, "znach": new_znach}
        data["Carts"].append(new_kart)

        with open('Kart.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def display_cartu(self):
        with open('Kart.json', 'r', encoding="utf-8") as Card:
            data = json.load(Card)
            vvod = random.choice(data['Carts'])
            sllov = vvod.get('slovo')
            znach = vvod.get('znach')
            self.cartu.set(sllov)
            self.znach.set(znach)
