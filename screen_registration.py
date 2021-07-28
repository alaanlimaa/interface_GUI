import tkinter as tk


class TelaCadastro:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.cadastroTela = tk.Tk()
        self.cadastroTela.geometry("477x450+432+174")
        self.cadastroTela.minsize(120, 1)
        self.cadastroTela.maxsize(2736, 751)
        self.cadastroTela.resizable(1,  1)
        self.cadastroTela.title("Cadastro")
        self.cadastroTela.configure(background="#7da6e3")

        self.Label1 = tk.Label(self.cadastroTela)
        self.Label1.place(relx=0.335, rely=0.067, height=41, width=146)
        self.Label1.configure(background="#7da6e3")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Viner Hand ITC} -size 24")
        self.Label1.configure(foreground="#f7ec22")
        self.Label1.configure(text='''Cadastro''')

        self.Label2 = tk.Label(self.cadastroTela)
        self.Label2.place(relx=0.126, rely=0.178, height=21, width=84)
        self.Label2.configure(anchor='nw')
        self.Label2.configure(background="#7da6e3")
        self.Label2.configure(borderwidth="0")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 11")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Nome:''')

        self.Label3 = tk.Label(self.cadastroTela)
        self.Label3.place(relx=0.126, rely=0.267, height=21, width=134)
        self.Label3.configure(anchor='nw')
        self.Label3.configure(background="#7da6e3")
        self.Label3.configure(borderwidth="0")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 11")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Sobrenome:''')

        self.Label3_1 = tk.Label(self.cadastroTela)
        self.Label3_1.place(relx=0.126, rely=0.378, height=21, width=144)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(anchor='nw')
        self.Label3_1.configure(background="#7da6e3")
        self.Label3_1.configure(borderwidth="0")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font="-family {Segoe UI} -size 11")
        self.Label3_1.configure(foreground="#ffffff")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Usuário:''')

        self.Label3_1_1 = tk.Label(self.cadastroTela)
        self.Label3_1_1.place(relx=0.126, rely=0.578, height=21, width=144)
        self.Label3_1_1.configure(activebackground="#f9f9f9")
        self.Label3_1_1.configure(activeforeground="black")
        self.Label3_1_1.configure(anchor='nw')
        self.Label3_1_1.configure(background="#7da6e3")
        self.Label3_1_1.configure(borderwidth="0")
        self.Label3_1_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1_1.configure(font="-family {Segoe UI} -size 11")
        self.Label3_1_1.configure(foreground="#ffffff")
        self.Label3_1_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1_1.configure(highlightcolor="black")
        self.Label3_1_1.configure(text='''Senha:''')

        self.Label3_1_2 = tk.Label(self.cadastroTela)
        self.Label3_1_2.place(relx=0.126, rely=0.467, height=21, width=144)
        self.Label3_1_2.configure(activebackground="#f9f9f9")
        self.Label3_1_2.configure(activeforeground="black")
        self.Label3_1_2.configure(anchor='nw')
        self.Label3_1_2.configure(background="#7da6e3")
        self.Label3_1_2.configure(borderwidth="0")
        self.Label3_1_2.configure(disabledforeground="#a3a3a3")
        self.Label3_1_2.configure(font="-family {Segoe UI} -size 11")
        self.Label3_1_2.configure(foreground="#ffffff")
        self.Label3_1_2.configure(highlightbackground="#d9d9d9")
        self.Label3_1_2.configure(highlightcolor="black")
        self.Label3_1_2.configure(text='''Contato (ddd):''')

        self.Label3_1_3 = tk.Label(self.cadastroTela)
        self.Label3_1_3.place(relx=0.545, rely=0.578, height=21, width=144)
        self.Label3_1_3.configure(activebackground="#f9f9f9")
        self.Label3_1_3.configure(activeforeground="black")
        self.Label3_1_3.configure(anchor='nw')
        self.Label3_1_3.configure(background="#7da6e3")
        self.Label3_1_3.configure(borderwidth="0")
        self.Label3_1_3.configure(disabledforeground="#a3a3a3")
        self.Label3_1_3.configure(font="-family {Segoe UI} -size 11")
        self.Label3_1_3.configure(foreground="#ffffff")
        self.Label3_1_3.configure(highlightbackground="#d9d9d9")
        self.Label3_1_3.configure(highlightcolor="black")
        self.Label3_1_3.configure(text='''Confirme a senha:''')

        self.nome = tk.Entry(self.cadastroTela)
        self.nome.place(relx=0.126, rely=0.222, height=20, relwidth=0.763)
        self.nome.configure(background="white")
        self.nome.configure(disabledforeground="#a3a3a3")
        self.nome.configure(font="TkFixedFont")
        self.nome.configure(foreground="#000000")
        self.nome.configure(insertbackground="black")

        self.sobrenome = tk.Entry(self.cadastroTela)
        self.sobrenome.place(relx=0.126, rely=0.311, height=20, relwidth=0.763)
        self.sobrenome.configure(background="white")
        self.sobrenome.configure(disabledforeground="#a3a3a3")
        self.sobrenome.configure(font="TkFixedFont")
        self.sobrenome.configure(foreground="#000000")
        self.sobrenome.configure(insertbackground="black")

        self.usuario = tk.Entry(self.cadastroTela)
        self.usuario.place(relx=0.126, rely=0.422, height=20, relwidth=0.763)
        self.usuario.configure(background="white")
        self.usuario.configure(disabledforeground="#a3a3a3")
        self.usuario.configure(font="TkFixedFont")
        self.usuario.configure(foreground="#000000")
        self.usuario.configure(insertbackground="black")

        self.contato = tk.Entry(self.cadastroTela)
        self.contato.place(relx=0.126, rely=0.511, height=20, relwidth=0.763)
        self.contato.configure(background="white")
        self.contato.configure(disabledforeground="#a3a3a3")
        self.contato.configure(font="TkFixedFont")
        self.contato.configure(foreground="#000000")
        self.contato.configure(insertbackground="black")
        self.contato.bind("<KeyRelease>", self.formatar_contato, self.contato.pack)

        self.senha = tk.Entry(self.cadastroTela, show='*')
        self.senha.place(relx=0.126, rely=0.622, height=20, relwidth=0.323)
        self.senha.configure(background="white")
        self.senha.configure(disabledforeground="#a3a3a3")
        self.senha.configure(font="TkFixedFont")
        self.senha.configure(foreground="#000000")
        self.senha.configure(insertbackground="black")

        self.confirmaSenha = tk.Entry(self.cadastroTela, show='*')
        self.confirmaSenha.place(relx=0.545, rely=0.622, height=20, relwidth=0.344)
        self.confirmaSenha.configure(background="white")
        self.confirmaSenha.configure(cursor="fleur")
        self.confirmaSenha.configure(disabledforeground="#a3a3a3")
        self.confirmaSenha.configure(font="TkFixedFont")
        self.confirmaSenha.configure(foreground="#000000")
        self.confirmaSenha.configure(insertbackground="black")

        self.Button1Cadastrar = tk.Button(self.cadastroTela, command=self.cadastrar_cliente)
        self.Button1Cadastrar.place(relx=0.356, rely=0.733, height=34, width=147)
        self.Button1Cadastrar.configure(activebackground="#ececec")
        self.Button1Cadastrar.configure(activeforeground="#000000")
        self.Button1Cadastrar.configure(background="#f7ec22")
        self.Button1Cadastrar.configure(borderwidth="5")
        self.Button1Cadastrar.configure(disabledforeground="#a3a3a3")
        self.Button1Cadastrar.configure(foreground="#000000")
        self.Button1Cadastrar.configure(highlightbackground="#d9d9d9")
        self.Button1Cadastrar.configure(highlightcolor="black")
        self.Button1Cadastrar.configure(pady="0")
        self.Button1Cadastrar.configure(text='''Cadastrar''')

        self.cadastroTela.mainloop()

    def formatar_contato(self, event=None):
        interface = self.contato.get()[:14]
        contato = '('
        if event.keysym.lower() == "backspace":
            return
        for index in range(len(interface)):
            if not interface[index] in '0123456789':
                continue
            if index == 0:
                contato += interface[index]
            elif index == 2:
                contato += interface[index] + ')'
            elif index == 8:
                contato += interface[index] + '-'
            else:
                contato += interface[index]

        self.contato.delete(0, "end")
        self.contato.insert(0, contato)

    def cadastrar_cliente(self):
        nome = self.nome.get().title().strip()
        sobrenome = self.sobrenome.get().title().strip()
        usuario = self.usuario.get().strip()
        contato = self.contato.get()
        senha = self.senha.get().strip()
        confSenha = self.confirmaSenha.get().strip()
        if self.confirmaSenha.get() == self.senha.get() != '':
            clientes = (nome, sobrenome, usuario, contato, senha, confSenha)
            with open('dados.txt', 'a') as arquidoDados:
                arquidoDados.write(f'{clientes}\n')
        else:
            print('Usuário não cadastrado, campos obrigatórios')
        self.cadastroTela.destroy()


TelaCadastro()
