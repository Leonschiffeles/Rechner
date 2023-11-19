import Gui as gu


def ekonomka():
    gu.tk.Label(gu.frame_Head, text="  Э  К  О  Н  О  М  К  А  ",
                width=50, height=100, bg="#5F837F", fg="#938FA6", font=('times', 20, 'bold')).pack()

    gu.tk.Label(gu.frame_Body, text="Oжидается в скором времени", fg='#938FA6',
                bg='#5F837F', width=50, font=("Arial", 24)).pack(pady=150)
