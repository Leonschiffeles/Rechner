import Gui as gu
import Kartochka as ka
import json


def display_title():
    gu.tk.Label(gu.frame_Head, text="   Э    К    О    Н    О    М    К    А   ",
                width=50, height=100, fg='#B7BCD0', bg='#5F837F', font=('times', 20, 'bold')).pack()


class Ekonomka:
    def __init__(self):
        display_title()
        self.obyaz = gu.tk.IntVar()
        self.razvl = gu.tk.IntVar()
        self.transport = gu.tk.IntVar()
        self.eda = gu.tk.IntVar()
        self.vsego = gu.tk.IntVar()
        self.display_dob()
        self.vsegototal()

        self.dob_obyaz = gu.tk.Entry(gu.frame_Body, width=15, bg="#FFFFFF", fg="#5F837F", justify="center",
                                     font=('times', 20, 'bold'))
        self.dob_obyaz.grid(row=0, column=0, padx=35, pady=15)

        self.dob_razvl = gu.tk.Entry(gu.frame_Body, width=15, bg="#FFFFFF", fg="#5F837F", justify="center",
                                     font=('times', 20, 'bold'))
        self.dob_razvl.grid(row=1, column=0, padx=35, pady=15)

        self.dob_transport = gu.tk.Entry(gu.frame_Body, width=15, bg="#FFFFFF", fg="#5F837F", justify="center",
                                         font=('times', 20, 'bold'))
        self.dob_transport.grid(row=2, column=0, padx=35, pady=15)

        self.dob_eda = gu.tk.Entry(gu.frame_Body, width=15, bg="#FFFFFF", fg="#5F837F", justify="center",
                                   font=('times', 20, 'bold'))
        self.dob_eda.grid(row=3, column=0, padx=35, pady=15)

        self.vsego.trace_add('write', lambda *args: self.l_vsego.config(text=self.vsego.get()))
        self.obyaz.trace_add('write', lambda *args: self.l_obyaz.config(text=self.obyaz.get()))
        self.razvl.trace_add('write', lambda *args: self.l_raz.config(text=self.razvl.get()))
        self.transport.trace_add('write', lambda *args: self.l_trans.config(text=self.transport.get()))
        self.eda.trace_add('write', lambda *args: self.l_eda.config(text=self.eda.get()))

        self.l_vsego = gu.tk.Label(gu.frame_Body, textvariable=self.vsego, width=35, fg='#B7BCD0', bg='#5F837F',
                                   font=('times', 20, 'bold')).grid(row=4, column=1, padx=6, pady=15)
        self.l_obyaz = gu.tk.Label(gu.frame_Body, textvariable=self.obyaz, width=35, fg='#B7BCD0', bg='#5F837F',
                                   font=('times', 20, 'bold')).grid(row=0, column=1, padx=6, pady=15)
        self.l_raz = gu.tk.Label(gu.frame_Body, textvariable=self.razvl, width=35, fg='#B7BCD0', bg='#5F837F',
                                 font=('times', 20, 'bold')).grid(row=1, column=1, padx=6, pady=15)
        self.l_trans = gu.tk.Label(gu.frame_Body, textvariable=self.transport, width=35, fg='#B7BCD0', bg='#5F837F',
                                   font=('times', 20, 'bold')).grid(row=2, column=1, padx=6, pady=15)
        self.l_eda = gu.tk.Label(gu.frame_Body, textvariable=self.eda, width=35, fg='#B7BCD0', bg='#5F837F',
                                 font=('times', 20, 'bold')).grid(row=3, column=1, padx=6, pady=15)

        gu.tk.Button(gu.frame_Button, text="Добавить в список", width=20, height=2, activebackground='#B7BCD0',
                     activeforeground='#5F837F', fg='#B7BCD0',
                     bg='#5F837F', font=('times', 15, 'bold'), command=self.dob_dob).grid(row=0, column=0, padx=11,
                                                                                          pady=2)
        gu.tk.Button(gu.frame_Button, text="Обновление спискa", width=20, height=2,activebackground='#B7BCD0',
                     activeforeground='#5F837F', fg='#B7BCD0',
                     bg='#5F837F', font=('times', 15, 'bold'), command=self.obnov_str).grid(row=0, column=1, padx=6,
                                                                                            pady=2)

        gu.tk.Button(gu.frame_Button, text="Очистить список", width=20, height=2, activebackground='#B7BCD0',
                     activeforeground='#5F837F', fg='#B7BCD0',
                     bg='#5F837F', font=('times', 15, 'bold'), command=self.udalit_dob).grid(row=0, column=2, padx=6,
                                                                                             pady=2)

    def dob_dob(self):
        new_obyaz = int(self.dob_obyaz.get())
        new_razvl = int(self.dob_razvl.get())
        new_transport = int(self.dob_transport.get())
        new_eda = int(self.dob_eda.get())

        with open('Ekonomka.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        nov_poz = {"obyaz": new_obyaz, "razvl": new_razvl, "transport": new_transport, "eda": new_eda}
        data["Carts"].append(nov_poz)

        with open('Ekonomka.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def display_dob(self):
        with open('Ekonomka.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        kateg = data.get("Carts", [])

        sum_eda = 0
        sum_transport = 0
        sum_razvl = 0
        sum_obyaz = 0
        for cart in kateg:
            obyaz_value = int(cart.get("obyaz", 0))
            eda_value = int(cart.get("eda", 0))
            transport_value = int(cart.get("transport", 0))
            razvl_value = int(cart.get("razvl", 0))

            sum_eda += eda_value
            sum_transport += transport_value
            sum_razvl += razvl_value
            sum_obyaz += obyaz_value
            self.obyaz.set(f"Oбязательные расходы: {sum_obyaz}")
            self.razvl.set(f"Развлечения и отдых: {sum_razvl}")
            self.transport.set(f"Транспортные расходы: {sum_transport}")
            self.eda.set(f"Расходы на питание: {sum_eda}")

    def vsegototal(self):
        with open('Ekonomka.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        total = 0
        for cart in data.get("Carts", []):
            total += cart.get("obyaz", 0) + cart.get("razvl", 0) + cart.get("transport", 0) + cart.get("eda", 0)
            self.vsego.set(f" Bсего : {total}")

    def udalit_dob(self):
        new_data = {
            "Carts": [
                {
                    "obyaz": 0,
                    "razvl": 0,
                    "transport": 0,
                    "eda": 0
                }
            ]
        }

        with open('Ekonomka.json', 'w') as f:
            json.dump(new_data, f, indent=2)

    def obnov_str(self):
        ka.ekonomka()
