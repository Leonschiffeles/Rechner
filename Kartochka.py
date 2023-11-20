import Gui as gu
import Kartochki as ki
import Woprosu as wp
import Ekonomka as ek
import Quele as qu


def clear_Head():
    for widget in gu.frame_Head.winfo_children():
        widget.destroy()


def clear_Body():
    for widget in gu.frame_Body.winfo_children():
        widget.destroy()


def clear_Button():
    for widget in gu.frame_Button.winfo_children():
        widget.destroy()


def clear_Footer():
    for widget in gu.frame_Footer.winfo_children():
        widget.destroy()


def wiktorina():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    wp.Wiktorin()


def kartohk():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    ki.Carten()


def ekonomka():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    ek.Ekonomka()


def qule():
    clear_Head()
    clear_Body()
    clear_Button()
    clear_Footer()
    qu.Quele()
