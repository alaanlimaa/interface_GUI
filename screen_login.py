import tkinter as tk

class TelaLogin:
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           loginTela is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.loginTela = tk.Tk()
        self.loginTela.geometry("419x450+437+144")
        self.loginTela.minsize(120, 1)
        self.loginTela.maxsize(2736, 751)
        self.loginTela.resizable(1, 1)
        self.loginTela.title("Login")
        self.loginTela.configure(background="#7da6e3")

        self.Label1 = tk.Label(self.loginTela)
        self.Label1.place(relx=0.317, rely=0.111, height=61, width=172)
        self.Label1.configure(background="#7da6e3")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Viner Hand ITC} -size 24")
        self.Label1.configure(foreground="#f7ec22")
        self.Label1.configure(text='''Login''')

        self.menubar = tk.Menu(self.loginTela, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        self.loginTela.configure(menu=self.menubar)

        self.Label2 = tk.Label(self.loginTela)
        self.Label2.place(relx=0.186, rely=0.311, height=21, width=126)
        self.Label2.configure(anchor='nw')
        self.Label2.configure(background="#7da6e3")
        self.Label2.configure(borderwidth="0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 11")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Usuário:''')

        self.Label3 = tk.Label(self.loginTela)
        self.Label3.place(relx=0.186, rely=0.444, height=21, width=137)
        self.Label3.configure(anchor='nw')
        self.Label3.configure(background="#7da6e3")
        self.Label3.configure(borderwidth="0")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 11")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Senha:''')

        self.Usuario = tk.Entry(self.loginTela)
        self.Usuario.place(relx=0.186, rely=0.378, height=20, relwidth=0.63)
        self.Usuario.configure(background="white")
        self.Usuario.configure(disabledforeground="#a3a3a3")
        self.Usuario.configure(font="TkFixedFont")
        self.Usuario.configure(foreground="#000000")
        self.Usuario.configure(insertbackground="black")

        self.Senha = tk.Entry(self.loginTela, show='*')
        self.Senha.place(relx=0.186, rely=0.511, height=20, relwidth=0.63)
        self.Senha.configure(background="white")
        self.Senha.configure(disabledforeground="#a3a3a3")
        self.Senha.configure(font="TkFixedFont")
        self.Senha.configure(foreground="#000000")
        self.Senha.configure(insertbackground="black")

        self.Button1Entrar = tk.Button(self.loginTela)
        self.Button1Entrar.place(relx=0.239, rely=0.6, height=34, width=97)
        self.Button1Entrar.configure(activebackground="#ececec")
        self.Button1Entrar.configure(activeforeground="#000000")
        self.Button1Entrar.configure(background="#f7ec22")
        self.Button1Entrar.configure(borderwidth="5")
        self.Button1Entrar.configure(disabledforeground="#a3a3a3")
        self.Button1Entrar.configure(foreground="#000000")
        self.Button1Entrar.configure(highlightbackground="#d9d9d9")
        self.Button1Entrar.configure(highlightcolor="black")
        self.Button1Entrar.configure(pady="0")
        self.Button1Entrar.configure(text='''Entrar''')

        self.Button2Cadastrar = tk.Button(self.loginTela, command=self.cadastrar_cliente)
        self.Button2Cadastrar.place(relx=0.525, rely=0.6, height=34, width=97)
        self.Button2Cadastrar.configure(activebackground="#ececec")
        self.Button2Cadastrar.configure(activeforeground="#000000")
        self.Button2Cadastrar.configure(background="#f7ec22")
        self.Button2Cadastrar.configure(borderwidth="5")
        self.Button2Cadastrar.configure(disabledforeground="#a3a3a3")
        self.Button2Cadastrar.configure(foreground="#000000")
        self.Button2Cadastrar.configure(highlightbackground="#d9d9d9")
        self.Button2Cadastrar.configure(highlightcolor="black")
        self.Button2Cadastrar.configure(pady="0")
        self.Button2Cadastrar.configure(text='''Cadastrar-se''')

        self.Button3Cancelar = tk.Button(self.loginTela, command=self.loginTela.destroy)
        self.Button3Cancelar.place(relx=0.358, rely=0.733, height=34, width=117)
        self.Button3Cancelar.configure(activebackground="#ececec")
        self.Button3Cancelar.configure(activeforeground="#000000")
        self.Button3Cancelar.configure(background="#f7ec22")
        self.Button3Cancelar.configure(borderwidth="5")
        self.Button3Cancelar.configure(disabledforeground="#a3a3a3")
        self.Button3Cancelar.configure(foreground="#000000")
        self.Button3Cancelar.configure(highlightbackground="#d9d9d9")
        self.Button3Cancelar.configure(highlightcolor="black")
        self.Button3Cancelar.configure(pady="0")
        self.Button3Cancelar.configure(text='''Cancelar''')

        self.loginTela.mainloop()

    def cadastrar_cliente(self):
        print('Cadastrado')
        import screen_registration as cd
        cd.TelaCadastro()

TelaLogin()


