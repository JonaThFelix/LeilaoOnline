# Projeto da faculdade simulando um leilão online
# O intuito do projeto é ser literalmente simples, foi usado o tkinter para geração da interface.
# {iO$tream}

import tkinter as tk
from tkinter import ttk

class Exercicio01:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Leilão Online")

       
        estilo = ttk.Style()
        estilo.theme_use('clam')  # Mudando para um tema leve
        estilo.configure('TFrame', background='#cfe2f3')  # Cor de fundo do Frame
        estilo.configure('TLabel', background='#F0FFFF')  # Cor de fundo dos rótulos
        estilo.configure('TButton', background='#008000', foreground='black')  # Cores dos botões


        # ----------------------------------------- Dicionário de armazenamento dos dados --------------------------------------------------#

        self.usuarios = {}
        self.itens_leilao = {}
        self.lances = {}
        self.leiloes_em_andamento = {}

        # -------------------------------------------- Tela de cadastro ------------------------------------------------------------------#

        self.tela_cadastro = ttk.LabelFrame(self.root, text="Cadastro de Usuários")
        self.tela_cadastro.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.tela_cadastro, text="Nome de usuário:").grid(row=0, column=0, sticky="w")
        self.entry_nome_usuario = ttk.Entry(self.tela_cadastro)
        self.entry_nome_usuario.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.tela_cadastro, text="Senha:").grid(row=1, column=0, sticky="w")
        self.entry_senha = ttk.Entry(self.tela_cadastro, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.btn_cadastrar = ttk.Button(self.tela_cadastro, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.grid(row=2, columnspan=2, pady=5)

        # -------------------------------------------- Listagem dos Itens ------------------------------------------------------------------#

        self.tela_itens = ttk.LabelFrame(self.root, text="Listagem de Itens")
        self.tela_itens.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.tela_itens, text="Nome do Item:").grid(row=0, column=0, sticky="w")
        self.entry_nome_item = ttk.Entry(self.tela_itens)
        self.entry_nome_item.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.tela_itens, text="Descrição:").grid(row=1, column=0, sticky="w")
        self.entry_descricao = ttk.Entry(self.tela_itens)
        self.entry_descricao.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(self.tela_itens, text="Valor Inicial:").grid(row=2, column=0, sticky="w")
        self.entry_valor_inicial = ttk.Entry(self.tela_itens)
        self.entry_valor_inicial.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.btn_iniciar_leilao = ttk.Button(self.tela_itens, text="Iniciar Leilão", command=self.iniciar_leilao)
        self.btn_iniciar_leilao.grid(row=3, columnspan=2, pady=5)

        self.listbox_itens = tk.Listbox(self.tela_itens)
        self.listbox_itens.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # -------------------------------------------- Tela de Lances  ------------------------------------------------------------------#

        '''
        Importante que aqui preferi fazer com que caso dê 5 lances em um leilão, o com maior valor irá vencer consequentemente, 
        caso seja cadastrado um outro item, o usuário deverá clicar no segundo item e iniciar o lance do leilão, caso contrátio
        puxaria o mesmo item.
        '''

        self.tela_lances = ttk.LabelFrame(self.root, text="Colocação de Lances")
        self.tela_lances.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.tela_lances, text="Valor do Lance:").grid(row=0, column=0, sticky="w")
        self.entry_valor_lance = ttk.Entry(self.tela_lances)
        self.entry_valor_lance.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        #Teste
        #self.tela_arrematante
        ttk.Label(self.tela_lances, text="Arrematante:").grid(row=1, column=0, sticky="w")
        self.entry_valor_arrematante = ttk.Entry(self.tela_lances)
        self.entry_valor_arrematante.grid(row=1, column=1, padx=5, pady=5, sticky="ew")



        self.btn_colocar_lance = ttk.Button(self.tela_lances, text="Colocar Lance", command=self.colocar_lance)
        self.btn_colocar_lance.grid(row=2, columnspan=2, pady=6)

        # -------------------------------------------- Tela com lances  ------------------------------------------------------------------#
        self.listbox_lances = tk.Listbox(self.tela_lances)
        self.listbox_lances.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Contador de lances
        self.num_lances = 0

    def cadastrar_usuario(self):
        nome_usuario = self.entry_nome_usuario.get()
        senha = self.entry_senha.get()
        self.usuarios[nome_usuario] = senha
        print("Usuário cadastrado:", nome_usuario)

    def iniciar_leilao(self):
        nome_item = self.entry_nome_item.get()
        descricao = self.entry_descricao.get()
        valor_inicial = float(self.entry_valor_inicial.get())

        self.itens_leilao[nome_item] = {"descricao": descricao, "valor_inicial": valor_inicial}
        self.listbox_itens.insert(tk.END, f"{nome_item}: {descricao} - Valor Inicial: {valor_inicial}")

    def colocar_lance(self):
        if self.num_lances < 5:
            nome_item_selecionado = self.listbox_itens.get(tk.ACTIVE)
            valor_lance = float(self.entry_valor_lance.get())
            valor_arrematante = str(self.entry_valor_arrematante.get())


            nome_item = nome_item_selecionado.split(':')[0].strip()  # Obtém apenas o nome do item
            if nome_item in self.itens_leilao:
                self.lances.setdefault(nome_item, []).append(valor_lance)
                self.lances.setdefault(valor_arrematante, []).append(valor_arrematante) #Nome do Arrematante aqui

                

                print(f"Lance de {valor_lance} colocado para {nome_item}")
                self.num_lances += 1
                
                if self.num_lances == 5:
                    lances = self.lances[nome_item]
                    lance_vencedor = max(lances)
                    print(f"Lance vencedor para {nome_item}: {lance_vencedor}")
                    self.listbox_lances.insert(tk.END, f"Lance vencedor de {valor_arrematante} para o item {nome_item}: no valor de {lance_vencedor}")
                    self.num_lances = 0
                else:
                    self.listbox_lances.insert(tk.END, f"Lance de {valor_arrematante} para {nome_item}: {valor_lance}")
            else:
                print("Este item não está em leilão.")
        else:
            print("Limite de lances atingido para este item.")



if __name__ == "__main__":
    root = tk.Tk()
    app = Exercicio01(root)
    root.mainloop()
