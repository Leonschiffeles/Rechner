import Gui as gu


def qule():
    gu.tk.Label(gu.frame_Head, text="  И  С  Т  О  Ч  Н  И  К  И  ",
                width=50, height=100, bg="#D2F06A", fg="#5EB8C0", font=('times', 20, 'bold')).pack()

    gu.tk.Label(gu.frame_Body, text="Oжидается в скором времени", width=50, bg='#D2F06A',
                fg='#5EB8C0', font=("Arial", 24)).pack(pady=150)
