from tkinter import *
import tkinter.messagebox
import database

def criarTelaCentralizada(nome):
    tela = Tk(className=f' {nome} ')
    ws = tela.winfo_screenwidth()
    hs = tela.winfo_screenheight()
    tela.geometry(f'800x600+{int((ws/2)-(400))}+{int((hs/2)-(300))}')
    tela['background'] = "#32CD32"
    return tela


class Cadastro:
    def __init__(self, master=None):
        self.fontePadrao = ("Bahnschrift", "20")
        self.Cadastro=criarTelaCentralizada('Cadastro')


        self.titulo = Label(self.Cadastro, text="Cadastro", bg='#32CD32')
        self.titulo["font"] = ("Bahnschrift", "40","bold")
        self.titulo.place(x=290, y=30)

        self.nome=Label(self.Cadastro, text='NOME', bg='#32CD32')
        self.nome['font']=("Bahnschrift", "20", 'bold')
        self.nome.place(x=360, y=135)

        self.inputNome=Entry(self.Cadastro)
        self.inputNome['width']=20
        self.inputNome['font']=self.fontePadrao
        self.inputNome.place(x=250, y=180)

        self.senha=Label(self.Cadastro, text='SENHA', bg='#32CD32')
        self.senha['font']=("Bahnschrift", "20", 'bold')
        self.senha.place(x=350, y=230)

        self.inputSenha=Entry(self.Cadastro)
        self.inputSenha['width']=20
        self.inputSenha['font']=self.fontePadrao
        self.inputSenha['show']='*'
        self.inputSenha.place(x=250, y=275)

        self.senha2=Label(self.Cadastro, text='CONFIRME SUA SENHA', bg='#32CD32')
        self.senha2['font']=("Bahnschrift", "20", 'bold')
        self.senha2.place(x=260, y=340)

        self.inputSenha2=Entry(self.Cadastro)
        self.inputSenha2['width']=20
        self.inputSenha2['show']='*'
        self.inputSenha2['font']=self.fontePadrao
        self.inputSenha2.place(x=250, y=390)

        self.botaoCadastro=Button(self.Cadastro, text='Criar conta')
        self.botaoCadastro['font']=("Bahnschrift", "17",'bold')
        self.botaoCadastro['width']=15
        self.botaoCadastro['command']= self.verificaSenha
        self.botaoCadastro['relief']='raised'
        self.botaoCadastro['borderwidth']=5
        self.botaoCadastro.place(x=180, y=470)

        self.botaoVoltar=Button(self.Cadastro, text='Voltar')
        self.botaoVoltar['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar['width']=15
        self.botaoVoltar['command']= lambda:[self.Cadastro.destroy(),TelaInicial()]
        self.botaoVoltar['relief']='raised'
        self.botaoVoltar['borderwidth']=5
        self.botaoVoltar.place(x=420, y=470)

    #Método verificar senha
    def verificaSenha(self):
        nome = self.inputNome.get()
        senha2 = self.inputSenha2.get()
        senha = self.inputSenha.get()
        if senha != senha2:
            tkinter.messagebox.showerror(message = "Senha devem ser iguais !")
        else:
            criarConta = database.create_new_user(nome, senha)
            if not criarConta:
                tkinter.messagebox.showerror(message = "Senha deve conter:\n6 caracteres\nNo mínimo 1 letra maiúscula\nNo mínimo 1 letra minúscula\nNo mínimo 1 número")
            else:
                tkinter.messagebox.showinfo(message = "Conta cadastrada com sucesso !")



class Login:
    def __init__(self, master=None):
        self.fontePadrao = ("Bahnschrift", "20")
        self.Login=criarTelaCentralizada('Login')

        self.tituloLogin = Label(self.Login, text="Login", bg='#32CD32')
        self.tituloLogin["font"] = ("Bahnschrift", "40","bold")
        self.tituloLogin.place(x=330, y=30)

        self.nomeLogin=Label(self.Login, text='NOME', bg='#32CD32')
        self.nomeLogin['font']=("Bahnschrift", "20", 'bold')
        self.nomeLogin.place(x=360, y=160)

        self.inputNomeLogin=Entry(self.Login)
        self.inputNomeLogin['width']=20
        self.inputNomeLogin['font']=self.fontePadrao
        self.inputNomeLogin.place(x=250, y=210)

        self.senhaLogin=Label(self.Login, text='SENHA', bg='#32CD32')
        self.senhaLogin['font']=("Bahnschrift", "20", 'bold')
        self.senhaLogin.place(x=350, y=280)

        self.inputSenhaLogin=Entry(self.Login)
        self.inputSenhaLogin['width']=20
        self.inputSenhaLogin['font']=self.fontePadrao
        self.inputSenhaLogin['show']='*'
        self.inputSenhaLogin.place(x=250, y=330)


        self.botaoLogin=Button(self.Login, text='Entrar')
        self.botaoLogin['font']=("Bahnschrift", "17",'bold')
        self.botaoLogin['width']=15
        self.botaoLogin['command']= self.verificaLogin
        self.botaoLogin['relief']='raised'
        self.botaoLogin['borderwidth']=5
        self.botaoLogin.place(x=300, y=400)

        self.botaoVoltar2=Button(self.Login, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.Login.destroy(),TelaInicial()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=300, y=490)

    def verificaLogin(self):
        user = self.inputNomeLogin.get() #BOTAR AQUI INFO PRA DB P REALIZAR CADASTRO
        password = self.inputSenhaLogin.get()
        login = database.login(user, password)
        if not login:
            tkinter.messagebox.showerror(message = "Usuário e/ou senha incorretos !")
        else:
            tkinter.messagebox.showinfo(message = "Bem-vindo(a)")


class TelaInicial:
    def __init__(self, master=None):
        self.TelaInicial=criarTelaCentralizada('Tela Inicial')

        self.tituloInicial = Label(self.TelaInicial, text="Seja bem-vindo ao Snake Game!", bg='#32CD32')
        self.tituloInicial["font"] = ("Showcard Gothic", "32","bold")
        self.tituloInicial.place(x=40, y=30)

        self.botaoC=Button(self.TelaInicial, text='Cadastro')
        self.botaoC['font']=("Bahnschrift", "20",'bold')
        self.botaoC['width']=25
        self.botaoC['command']= lambda:[self.TelaInicial.destroy(), Cadastro()]
        self.botaoC['relief']='raised'
        self.botaoC['borderwidth']=5
        self.botaoC.place(x=200, y=180)

        self.botaoL=Button(self.TelaInicial, text='Login')
        self.botaoL['font']=("Bahnschrift", "20",'bold')
        self.botaoL['width']=25
        self.botaoL['command']= lambda:[self.TelaInicial.destroy(), Login()]
        self.botaoL['relief']='raised'
        self.botaoL['borderwidth']=5
        self.botaoL.place(x=200, y=300)

        self.botaoR=Button(self.TelaInicial, text='Ranking')
        self.botaoR['font']=("Bahnschrift", "20",'bold')
        self.botaoR['width']=25
        self.botaoR['command']= lambda:[self.TelaInicial.destroy(), RankingGeral()]
        self.botaoR['relief']='raised'
        self.botaoR['borderwidth']=5
        self.botaoR.place(x=200, y=420)

        self.TelaInicial.mainloop()
        
class RankingGeral:
    def __init__(self, master=None):
        self.RankingGeral=criarTelaCentralizada('Ranking Geral')

        self.tituloRankingG = Label(self.RankingGeral, text="Ranking", bg='#32CD32')
        self.tituloRankingG["font"] = ("Bahnschrift", "40","bold")
        self.tituloRankingG.place(x=290, y=30)

        self.botaoNormal=Button(self.RankingGeral, text='Normal')
        self.botaoNormal['font']=("Bahnschrift", "20",'bold')
        self.botaoNormal['width']=25
        self.botaoNormal['command']= lambda:[self.RankingGeral.destroy(), RankingNormal()]
        self.botaoNormal['relief']='raised'
        self.botaoNormal['borderwidth']=5
        self.botaoNormal.place(x=200, y=140)

        self.botaoSwap=Button(self.RankingGeral, text='Swap')
        self.botaoSwap['font']=("Bahnschrift", "20",'bold')
        self.botaoSwap['width']=25
        self.botaoSwap['command']= lambda:[self.RankingGeral.destroy(), RankingSwap()]
        self.botaoSwap['relief']='raised'
        self.botaoSwap['borderwidth']=5
        self.botaoSwap.place(x=200, y=260)

        self.botaoY=Button(self.RankingGeral, text='Yin Yang')
        self.botaoY['font']=("Bahnschrift", "20",'bold')
        self.botaoY['width']=25
        self.botaoY['command']= lambda:[self.RankingGeral.destroy(), RankingYinYang()]
        self.botaoY['relief']='raised'
        self.botaoY['borderwidth']=5
        self.botaoY.place(x=200, y=380)

        self.botaoVoltar2=Button(self.RankingGeral, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.RankingGeral.destroy(),TelaInicial()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)

class RankingNormal():
    def __init__(self, master=None):
        self.RankingNormal=criarTelaCentralizada('Ranking Normal')

        self.tituloRankingN = Label(self.RankingNormal, text="Ranking", bg='#32CD32')
        self.tituloRankingN["font"] = ("Bahnschrift", "40","bold")
        self.tituloRankingN.place(x=290, y=30)

        self.botaoF=Button(self.RankingNormal, text='Nível Fácil')
        self.botaoF['font']=("Bahnschrift", "20",'bold')
        self.botaoF['width']=25
        self.botaoF['command']= lambda:[self.RankingNormal.destroy(), Facil()]
        self.botaoF['relief']='raised'
        self.botaoF['borderwidth']=5
        self.botaoF.place(x=200, y=140)

        self.botaoM=Button(self.RankingNormal, text='Nível Médio')
        self.botaoM['font']=("Bahnschrift", "20",'bold')
        self.botaoM['width']=25
        self.botaoM['command']= lambda:[self.RankingNormal.destroy(), Medio()]
        self.botaoM['relief']='raised'
        self.botaoM['borderwidth']=5
        self.botaoM.place(x=200, y=260)

        self.botaoD=Button(self.RankingNormal, text='Nível Difícil')
        self.botaoD['font']=("Bahnschrift", "20",'bold')
        self.botaoD['width']=25
        self.botaoD['command']= lambda:[self.RankingNormal.destroy(), Dificil()]
        self.botaoD['relief']='raised'
        self.botaoD['borderwidth']=5
        self.botaoD.place(x=200, y=380)

        self.botaoVoltar2=Button(self.RankingNormal, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.RankingNormal.destroy(),RankingGeral()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)

class RankingSwap():
    def __init__(self, master=None):   #COLOCAR BANCO DE DADOS NESSAS CLASSES
        self.RankingSwap=criarTelaCentralizada('Ranking-Swap')

        self.tituloS=Label(self.RankingSwap, text='Ranking - Swap', bg='#32CD32')
        self.tituloS['font']=("Bahnschrift", "40",'bold')
        self.tituloS.place(x=200,y=30)


        self.botaoVoltar2=Button(self.RankingSwap, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.RankingSwap.destroy(),RankingGeral()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)
    
class RankingYinYang():
    def __init__(self, master=None):   #COLOCAR BANCO DE DADOS NESSAS CLASSES
        self.RankingYinYang=criarTelaCentralizada('Ranking-Fácil')

        self.tituloY=Label(self.RankingYinYang, text='Ranking - Yin Yang', bg='#32CD32')
        self.tituloY['font']=("Bahnschrift", "40",'bold')
        self.tituloY.place(x=190,y=30)


        self.botaoVoltar2=Button(self.RankingYinYang, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.RankingYinYang.destroy(),RankingGeral()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)


class Facil():
    def __init__(self, master=None):   #COLOCAR BANCO DE DADOS NESSAS CLASSES
        self.Facil=criarTelaCentralizada('Ranking-Fácil')

        self.tituloF=Label(self.Facil, text='Ranking - Nível Fácil', bg='#32CD32')
        self.tituloF['font']=("Bahnschrift", "40",'bold')
        self.tituloF.place(x=150,y=30)


        self.botaoVoltar2=Button(self.Facil, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.Facil.destroy(),RankingNormal()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)

class Medio():
    def __init__(self, master=None):
        self.Medio=criarTelaCentralizada('Ranking-Médio')

        self.tituloM=Label(self.Medio, text='Ranking - Nível Médio', bg='#32CD32')
        self.tituloM['font']=("Bahnschrift", "40",'bold')
        self.tituloM.place(x=150,y=30)

        self.botaoVoltar2=Button(self.Medio, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.Medio.destroy(),RankingNormal()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)

class Dificil():
    def __init__(self, master=None):
        self.Dificil=criarTelaCentralizada('Ranking-Difícil')

        self.tituloD=Label(self.Dificil, text='Ranking - Nível Difícil', bg='#32CD32')
        self.tituloD['font']=("Bahnschrift", "40",'bold')
        self.tituloD.place(x=150,y=30)

        self.botaoVoltar2=Button(self.Dificil, text='Voltar')
        self.botaoVoltar2['font']=("Bahnschrift", "17",'bold')
        self.botaoVoltar2['width']=15
        self.botaoVoltar2['command']= lambda:[self.Dificil.destroy(),RankingNormal()]
        self.botaoVoltar2['relief']='raised'
        self.botaoVoltar2['borderwidth']=5
        self.botaoVoltar2.place(x=290, y=490)