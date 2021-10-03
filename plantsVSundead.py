from tkinter import *
import requests
from bs4 import BeautifulSoup as bs

##### Globais #####
producaonft_mes = 0.0
diaria_mes = 3000
liquido_baby = 94
liquido_mama = 588
fundo_padrao1 = "gray69"

##### Janela #####
janela = Tk()
janela.title("Plants VS Undead")
janela.geometry("400x400")
janela.configure(bg="gray69")
pvu_icone = PhotoImage(file=r"pvu_icon20.png")
le_icone = PhotoImage(file=r"le_icon45.png")

##### Puxar Cotacao PVU ao Abrir #####
url_PVU = requests.get("https://www.coingecko.com/pt/moedas/plant-vs-undead-token")
soup = bs(url_PVU.text, "html.parser")

url_dolar = requests.get("https://www.remessaonline.com.br/cotacao/cotacao-dolar")
soup2 = bs(url_dolar.text, "html.parser")

PVU = soup.find('span', {'class': 'no-wrap'}).text[1:5]
PVU = PVU.replace(',', '.')
PVU = float(PVU)

DOLAR = soup2.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
DOLAR = DOLAR.replace(',', '.')
DOLAR = float(DOLAR)
preco = round(DOLAR * PVU, 2)


def MamaCheck():
    return valor_check.get()

##### Refresh Screen #####
def Atualizar():
    soma = 0
    total_nfts = 0
    producao_LE_Total = 0
    if e1.get() != "" and e1_hr.get() != "":
        e1Aux = int(e1.get())
        e1_hrAux = int(e1_hr.get())
        prod1 = ((e1Aux / e1_hrAux) * 720) - 190
        total_nfts += 1
        soma += prod1
    if e2.get() != "" and e2_hr.get() != "":
        e2Aux = int(e2.get())
        e2_hrAux = int(e2_hr.get())
        prod2 = ((e2Aux / e2_hrAux) * 720) - 190
        soma += prod2
        total_nfts += 1
    if e3.get() != "" and e3_hr.get() != "":
        e3Aux = int(e3.get())
        e3_hrAux = int(e3_hr.get())
        prod3 = ((e3Aux / e3_hrAux) * 720) - 190
        soma += prod3
        total_nfts += 1
    if e4.get() != "" and e4_hr.get() != "":
        e4Aux = int(e4.get())
        e4_hrAux = int(e4_hr.get())
        prod4 = ((e4Aux / e4_hrAux) * 720) - 190
        soma += prod4
        total_nfts += 1
    if e5.get() != "" and e5_hr.get() != "":
        e5Aux = int(e5.get())
        e5_hrAux = int(e5_hr.get())
        prod5 = ((e5Aux / e5_hrAux) * 720) - 190
        soma += prod5
        total_nfts += 1
    if e6.get() != "" and e6_hr.get() != "":
        e6Aux = int(e6.get())
        e6_hrAux = int(e6_hr.get())
        prod6 = ((e6Aux / e6_hrAux) * 720) - 190
        soma += prod6
        total_nfts += 1
    if MamaCheck() == 0:
        producao_LE_Total = round(soma + diaria_mes + liquido_mama * 5 + liquido_baby * (50 - (total_nfts * 10)), 1)
        producao_mensal["text"] = producao_LE_Total
    else:
        producao_LE_Total = round(soma + diaria_mes + liquido_baby * 50, 1)
        producao_mensal["text"] = producao_LE_Total
    if e7_rate.get() != None:
        aux_e7 = int(e7_rate.get())
        val_pvu["text"] = round(producao_LE_Total * 0.95 / aux_e7, 2)
        total_mensal = round((producao_LE_Total * 0.95 / aux_e7) * preco, 2)
        tot_mes["text"] = "R$" + str(total_mensal)


##### Superior Messages #####
Label(janela, text="Produção das NFTs", font=("Verdana", 10), bg=fundo_padrao1).place(x=10, y=1)
Label(janela, text="LE", font=("Verdana"), bg=fundo_padrao1).place(x=35, y=20)
Label(janela, text="HR", font=("Verdana"), bg=fundo_padrao1).place(x=80, y=20)
Label(janela, text="Sua NFT ocupa o slot da MAMA ?", font=("Verdana", 10), bg=fundo_padrao1).place(x=170, y=20)
Label(janela, text="Cotação PVU", font=("Verdana", 10), bg=fundo_padrao1).place(x=170, y=120)
t_rate = Label(janela, text="Rate", font=("Verdana", 10), bg=fundo_padrao1)
t_rate.place(x=170, y=80)

##### CheckBox #####
valor_check = IntVar()
check_mama = Checkbutton(janela, text="SIM", variable=valor_check, font=("verdana", 10), bg=fundo_padrao1)
check_mama.place(x=200, y=40)

##### Refresh Button #####
botao = Button(janela, width=20, text="Atualizar", command=Atualizar, bg=fundo_padrao1)
botao.place(x=200, y=180)

##### Input Boxes #####
e1 = Entry(janela, width=5, bd=4)
e1.place(x=30, y=40)
e1.insert(END, "1202")
e1_hr = Entry(janela, width=5, bd=4)
e1_hr.place(x=75, y=40)
e1_hr.insert(END, "108")

e2 = Entry(janela, width=5, bd=4)
e2.place(x=30, y=68)
e2.insert(END, "544")
e2_hr = Entry(janela, width=5, bd=4)
e2_hr.place(x=75, y=68)
e2_hr.insert(END, "60")

e3 = Entry(janela, width=5, bd=4)
e3.place(x=30, y=96)
e3.insert(END, "4540")
e3_hr = Entry(janela, width=5, bd=4)
e3_hr.place(x=75, y=96)
e3_hr.insert(END, "336")

e4 = Entry(janela, width=5, bd=4)
e4.place(x=30, y=124)
e4_hr = Entry(janela, width=5, bd=4)
e4_hr.place(x=75, y=124)

e5 = Entry(janela, width=5, bd=4)
e5.place(x=30, y=152)
e5_hr = Entry(janela, width=5, bd=4)
e5_hr.place(x=75, y=152)

e6 = Entry(janela, width=5, bd=4)
e6.place(x=30, y=180)
e6_hr = Entry(janela, width=5, bd=4)
e6_hr.place(x=75, y=180)

e7_rate = Entry(janela, width=4, bd=3)
e7_rate.insert(END, "550")
e7_rate.place(x=215, y=80)

##### Inferior Messages #####
t_LE = Label(janela, text="Produção Mensal", font=("Verdana", 10), bg=fundo_padrao1)
t_LE.place(x=125, y=220)
producao_mensal = Label(janela, text="", font=("Verdana", 10), bg=fundo_padrao1)
producao_mensal.place(x=160, y=240)
t_pvu = Label(janela, text="PVU Mensal", font=("Verdana", 10), bg=fundo_padrao1)
t_pvu.place(x=125, y=265)
val_pvu = Label(janela, text="", font=("Verdana", 10), bg=fundo_padrao1)
val_pvu.place(x=160, y=285)
icone_pvu = Label(janela, image=pvu_icone, bg=fundo_padrao1).place(x=205, y=285)
icone_le = Label(janela, image=le_icone, bg=fundo_padrao1).place(x=205, y=238)
cotacao_real = Label(janela, text="R$" + str(preco), font=("Verdana", 10), bg=fundo_padrao1)
cotacao_real.place(x=275, y=120)
Label(janela, text="Total Mensal", font=("Verdana", 10), bg=fundo_padrao1).place(x=125, y=315)
tot_mes = Label(janela, text="", font=("Verdana", 10), bg=fundo_padrao1)
tot_mes.place(x=160, y=335)

janela.mainloop()
