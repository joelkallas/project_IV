"""
from tkinter import *

from tkinter import ttk
window = Tk()
window.geometry('700x700')
window.title("Generaator")


def clicked():
    x1 = str(tundoo.get())
    x2 = str(tundhommik.get())
    x4 = str(akumaht.get())
    x5 = str(akudeARV.get())
    x6 = str(paevamin.get())
    x7 = str(laadijateArv_t.get())
    x8 = str(voolutugevus.get())
    x9 = str(laadimispnge.get())
    x10 = str(pinge.get())
    x11 = str(chk_state.get())
    x12 = str(luba.get())
    x13 = str(URL_url.get())
    x14 = str(pw.get())
    f = open("Laetud.txt", "w")

    f.write("Lubab_oosel_laadida: " + x11 + "\n")
    f.write("Esmane: " + x12 + "\n")
    f.write("Paeva_min_aku: " + x6 + "\n")
    f.write("Akude_Arv: " + x5 + "\n")
    f.write("Yhe_Aku_AH: " + x4 + "\n")
    f.write("Yhe_Aku_PingeV: " + x10 + "\n")
    f.write("Laadijate_Arv: " + x7 + "\n")
    f.write("Yhe_LaadijaA: " + x8 + "\n")
    f.write("LaadimisPinge: " + x9 + "\n")
    f.write("Varuaeg: 2")
    f.write("hommikuKELL: " + x2 + "\n")
    f.write("ohtu: " + x1 + "\n")
    f.write("URL: " + x13 + "\n")
    f.write("PW: " + x14 + "\n")
    f.close()


tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

chk_state = BooleanVar()
tab_control.add(tab1, text='General')
esmane_laadimine = Checkbutton(tab2, text='Esmanelaadimine', var=chk_state)
luba = BooleanVar()
lubab_ool = Checkbutton(tab2, text='Lubab öösel laadida', var=luba)
tab_control.add(tab2, text='Settings')

opt = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
akud = [1, 2, 4, 6, 8, 10, 12, 14, 16]
laadijaA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130, 140, 160, 170, 180, 190, 200]
ping = [12, 24, 48]
tundoo = IntVar()
tundhommik = IntVar()
paevamin = IntVar()
akumaht = IntVar()
akudeARV = IntVar()
laadijateArv_t = IntVar()
voolutugevus = IntVar()
laadimispnge = IntVar()
pinge = IntVar()

ookell = Spinbox(tab2, from_=0, to=24, width=5, textvariable=tundoo, state='readonly')
pealkiri2 = Label(tab2, text='Settings', font="Helvetica 18 bold", justify=LEFT)
ookell_text = Label(tab2, text='ÖöKell')
hommikuKell_text = Label(tab2, text='Hommiku kell')
hommikuKell = Spinbox(tab2, from_=0, to=24, width=5, textvariable=tundhommik, state='readonly')

paevamin_aku = Spinbox(tab2, from_=20, to=50, width=5, textvariable=paevamin, state='readonly')
paevamin_aku_text = Label(tab2, text='% mis aku  võib laskuda', justify=LEFT)
yheakumaht = Spinbox(tab2, values=opt, width=5, textvariable=akumaht, state='readonly')
yheakumaht_aku_text = Label(tab2, text='AH ühe aku maht (AH)', justify=LEFT)
akudearv = Spinbox(tab2, values=akud, width=5, textvariable=akudeARV, state='readonly')
akudearc_text = Label(tab2, text='Mitu akut', justify=LEFT)
laadijateArv = Spinbox(tab2, from_=1, to=10, width=5, textvariable=laadijateArv_t, state='readonly')
laadijateArv_text = Label(tab2, text='Mitu Laadijat', justify=LEFT)
laadija_A = Spinbox(tab2, values=laadijaA, width=5, textvariable=voolutugevus, state='readonly')
laadija_A_text = Label(tab2, text='Ühe laadija voolutugevus (A)', justify=LEFT)
laadimispinge = Spinbox(tab2, from_=12, to=30, width=5, textvariable=laadimispnge, state='readonly')
laadimispinge_text = Label(tab2, text='Ühe laadija Laadimis pinge(V)', justify=LEFT)
yheakupinge = Spinbox(tab2, value=ping, width=5, textvariable=pinge, state='readonly')
yheakupinge_text = Label(tab2, text='Väljund pinge(V)', justify=LEFT)
URL_url = Entry(tab2, width=8)
yrl = Label(tab2, text='URL', justify=LEFT)
pw = Entry(tab2, width=8)
PW_txt = Label(tab2, text='Parool', justify=LEFT)
btn = Button(tab2, text="Save", command=clicked)
tundoo.set(23)
tundhommik.set(8)
paevamin.set(50)
akumaht.set(200)
akudeARV.set(8)
paevamin.set(50)
laadijateArv_t.set(1)
voolutugevus.set(80)
laadimispnge.set(28)
pinge.set(24)
chk_state.set(True)  # set check state
luba.set(True)
laadimiste_arv_t, akutase, generaatorkutus, effect, yhetunni_laadimine = 1,1,1,1,1
def refreshed():
    global laadimiste_arv_t, akutase, generaatorkutus, effect, yhetunni_laadimine
    with open('log.txt')as f:
        lines = f.read().splitlines()
        for b in lines:
            b=b.split(":")
            if b[0] == "laadimisArv":
                laadimiste_arv_t = b[1]
            if b[0] == "akutase":
                akutase = b[1]
            if b[0] == "generaatori_kutus":
                generaatorkutus = b[1]
            if b[0] == "effektiivsus":
                effect = b[1]
            if b[0] == "yhetunnilaadimine":
                yhetunni_laadimine = b[1]
    f.close()
    window.update()
    return laadimiste_arv_t, akutase, generaatorkutus, effect, yhetunni_laadimine

laadimiste_arv_t, akutase, generaatorkutus, effect, yhetunni_laadimine=refreshed()
# --------------------General----------------------------#
pealkiri1= Label(tab1, text="Ülevaade",font="Helvetica 16 bold")
laadimiste_arv_txt = Label(tab1, text=laadimiste_arv_t,  bg="gray", font="Helvetica 10 bold")
laadimiste_arv_txt_selgitus = Label(tab1, text="Mitu korda on akusi laetud")
akutase_txt = Label(tab1, text=akutase, bg="gray", font="Helvetica 10 bold")
akutase_txt_selgitus = Label(tab1, text="Hetke aku tase %")
generaatorkutus_txt = Label(tab1, text=generaatorkutus, bg="gray", font="Helvetica 10 bold")
generaatorkutus_txt_selgitus = Label(tab1, text="Generaatori kütuse tase")
effect_txt = Label(tab1, text=effect, bg="gray", font="Helvetica 10 bold")
effect_txt_selgitus = Label(tab1, text="Kui hästi on töötand %")
yhetunni_laadimine_txt = Label(tab1, text=yhetunni_laadimine, bg="gray", font="Helvetica 10 bold")
yhetunni_laadimine_txt_selgitus = Label(tab1, text="Mitu % laeb akusi ühes tunnis")
btn1 = Button(tab1, text="Refresh", command=refreshed)





# ----------------------general tab--------------------#
pealkiri1.grid(column=0, row=0)


laadimiste_arv_txt.grid(column=0, row=1)
laadimiste_arv_txt_selgitus.grid(column=1, row=1)
akutase_txt.grid(column=0, row=2)
akutase_txt_selgitus.grid(column=1, row=2)
generaatorkutus_txt.grid(column=0, row=3)
generaatorkutus_txt_selgitus.grid(column=1, row=3)
effect_txt.grid(column=0, row=4)
effect_txt_selgitus.grid(column=1, row=4)
yhetunni_laadimine_txt.grid(column=0, row=5)
yhetunni_laadimine_txt_selgitus.grid(column=1, row=5)
btn1.grid(column=3, row=14)
# ----------------Setting tab----------------#
pealkiri2.grid(column=0, row=0)
ookell_text.grid(column=1, row=1)
ookell.grid(column=0, row=1)
hommikuKell_text.grid(column=1, row=2)
hommikuKell.grid(column=0, row=2)
paevamin_aku.grid(column=0, row=3)
paevamin_aku_text.grid(column=1, row=3)
yheakumaht.grid(column=0, row=4)
yheakumaht_aku_text.grid(column=1, row=4)
yheakupinge.grid(column=0, row=5)
yheakupinge_text.grid(column=1, row=5)
akudearv.grid(column=0, row=6)
akudearc_text.grid(column=1, row=6)
laadijateArv.grid(column=0, row=7)
laadijateArv_text.grid(column=1, row=7)
laadija_A.grid(column=0, row=8)
laadija_A_text.grid(column=1, row=8)
laadimispinge.grid(column=0, row=9)
laadimispinge_text.grid(column=1, row=9)
URL_url.grid(column=0, row=10)
yrl.grid(column=1, row=10)
pw.grid(column=0, row=11)
PW_txt.grid(column=1, row=11)
esmane_laadimine.grid(column=0, row=12)
lubab_ool.grid(column=0, row=13)
btn.grid(column=3, row=14)

tab_control.pack(expand=50, fill='both')
window.update()
window.mainloop()
"""