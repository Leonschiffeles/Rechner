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
        self.quest_number = 0
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
        self.label.config(text=question[self.quest_number])

    def radio_buttons(self):
        ques_list = []
        while len(ques_list) < 4:
            radio_btn = gu.tk.Radiobutton(gu.frame_Body, text=" ", variable=self.opt_selected, bg='#EDD154', fg='black',
                                          activebackground='#000000', activeforeground='#EDD154', width=30,
                                          value=len(ques_list) + 1, font=('times', 16))
            ques_list.append(radio_btn)
            radio_btn.pack(side='bottom', padx='20', pady='1')
        return ques_list

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.quest_number]:
            self.opts[val]['text'] = option
            val += 1

    def buttons(self):
        gu.tk.Button(gu.frame_Button, text="Далее", activebackground='#000000', activeforeground='#EDD154', width=20,
                     height=2, bg='#EDD154', fg='#000000', font=('times', 20, 'bold'), command=self.next_btn, ).pack(
            pady=3)

    def check_ans(self, w_no):
        if self.opt_selected.get() == answer[w_no]:
            return True

    def next_btn(self):

        if self.check_ans(self.quest_number):
            self.ball += 1
        self.quest_number += 1

        if self.quest_number == self.data_size:
            self.display_result()
        else:
            self.display_question()
            self.display_options()

    def display_result(self):
        errors = self.data_size - self.ball
        correct = f"Правильных ответов: {self.ball}"
        wrong = f"Неправильных ответов: {errors}"
        total = int(self.ball / self.data_size * 100)
        result = f"В итоге: {total}%"
        mb.showinfo("", f"{result}\n{correct}\n{wrong}")
