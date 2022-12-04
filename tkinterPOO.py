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
        self.botaoR['command']= lambda:[self.TelaInicial.destroy(), Ranking()]
        self.botaoR['relief']='raised'
        self.botaoR['borderwidth']=5
        self.botaoR.place(x=200, y=420)

        self.TelaInicial.mainloop()
        
class Ranking:
    def __init__(self, master=None):
        self.Ranking=criarTelaCentralizada('Ranking')

        self.tituloRanking = Label(self.Ranking, text="Ranking", bg='#32CD32')
        self.tituloRanking["font"] = ("Bahnschrift", "40","bold")
        self.tituloRanking.place(x=290, y=30)

        self.botaoF=Button(self.Ranking, text='Nível Fácil')
        self.botaoF['font']=("Bahnschrift", "20",'bold')
        self.botaoF['width']=25
        self.botaoF['command']= lambda:[self.Ranking.destroy(), Facil()]
        self.botaoF['relief']='raised'
        self.botaoF['borderwidth']=5
        self.botaoF.place(x=200, y=180)

        self.botaoM=Button(self.Ranking, text='Nível Médio')
        self.botaoM['font']=("Bahnschrift", "20",'bold')
        self.botaoM['width']=25
        self.botaoM['command']= lambda:[self.Ranking.destroy(), Medio()]
        self.botaoM['relief']='raised'
        self.botaoM['borderwidth']=5
        self.botaoM.place(x=200, y=300)

        self.botaoD=Button(self.Ranking, text='Nível Difícil')
        self.botaoD['font']=("Bahnschrift", "20",'bold')
        self.botaoD['width']=25
        self.botaoD['command']= lambda:[self.Ranking.destroy(), Dificil()]
        self.botaoD['relief']='raised'
        self.botaoD['borderwidth']=5
        self.botaoD.place(x=200, y=420)

    
class Facil():
    def __init__(self, master=None):   #COLOCAR BANCO DE DADOS NESSAS CLASSES
        self.Facil=criarTelaCentralizada('Ranking-Fácil')

        self.tituloF=Label(self.Facil, text='Ranking - Nível Fácil', bg='#32CD32')
        self.tituloF['font']=("Bahnschrift", "40",'bold')
        self.tituloF.place(x=150,y=30)

class Medio():
    def __init__(self, master=None):
        self.Medio=criarTelaCentralizada('Ranking-Médio')

        self.tituloM=Label(self.Facil, text='Ranking - Nível Médio', bg='#32CD32')
        self.tituloM['font']=("Bahnschrift", "40",'bold')
        self.tituloM.place(x=150,y=30)

class Dificil():
    def __init__(self, master=None):
        self.Dificil=criarTelaCentralizada('Ranking-Difícil')

        self.tituloD=Label(self.Facil, text='Ranking - Nível Médio', bg='#32CD32')
        self.tituloD['font']=("Bahnschrift", "40",'bold')
        self.tituloD.place(x=150,y=30)