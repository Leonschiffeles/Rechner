from tkinter import messagebox as mb
import json
import Gui as gu

with open('woprosu.json', encoding="utf-8") as wikt:  # Ох и долго же я с этой строкой мучился...
    data = json.load(wikt)
question = (data['wopros'])
options = (data['wariant'])
answer = (data['otwet'])


def display_title():
    gu.tk.Label(gu.frame_Head, text="  В   И   К   Т   О   Р   И   Н   А  ",
                width=50, height=100, bg="#EDD154", fg="#000000", font=('times', 20, 'bold')).pack()


class Wiktorin:
    def __init__(self):
        self.w_no = 0
        self.label = gu.tk.Label(gu.frame_Body, text="", width=50, bg='#EDD154', fg='#000000',
                                 font=('times', 22, 'bold'))
        display_title()
        self.display_question()
        self.opt_selected = gu.tk.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.ball = 0

    def display_question(self):
        self.label.pack(pady='40', padx='20')
        self.label.config(text=question[self.w_no])

    def radio_buttons(self):
        w_spisok = []
        while len(w_spisok) < 4:
            radio_btn = gu.tk.Radiobutton(gu.frame_Body, text=" ", variable=self.opt_selected, bg='#EDD154', fg='black',
                                          activebackground='#000000', activeforeground='#EDD154', width=25,
                                          value=len(w_spisok) + 1, font=('times', 20))
            w_spisok.append(radio_btn)
            radio_btn.pack(side='bottom', padx='20', pady='1')
        return w_spisok

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.w_no]:
            self.opts[val]['text'] = option
            val += 1

    def buttons(self):
        gu.tk.Button(gu.frame_Button, text="Далее", activebackground='#000000', activeforeground='#EDD154', width=20,
                     height=2, bg='#EDD154', fg='#000000', font=('times', 20, 'bold'), command=self.next_btn,).pack()

    def check_ans(self, w_no):
        if self.opt_selected.get() == answer[w_no]:
            return True

    def next_btn(self):

        if self.check_ans(self.w_no):
            self.ball += 1
        self.w_no += 1

        if self.w_no == self.data_size:
            self.display_result()
        else:
            self.display_question()
            self.display_options()

    def display_result(self):
        oschibki = self.data_size - self.ball
        verno = f"Правильных ответов: {self.ball}"
        neverno = f"Неправильных ответов: {oschibki}"
        itogo = int(self.ball / self.data_size * 100)
        resultat = f"В итоге: {itogo}%"
        mb.showinfo("", f"{resultat}\n{verno}\n{neverno}")
