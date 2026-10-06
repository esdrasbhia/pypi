import customtkinter as ctk

# Configurações globais de tema
ctk.set_appearance_mode("System")  # Opções: "System", "Dark", "Light"
ctk.set_default_color_theme("blue") # Opções: "blue", "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Minha Aplicação CustomTkinter")
        self.geometry("400x350")

        # Título / Label
        self.label = ctk.CTkLabel(self, text="Bem-vindo!", font=("Helvetica", 20, "bold"))
        self.label.pack(padx=20, pady=(20, 10))

        # Campo de Entrada (Entry)
        self.entry = ctk.CTkEntry(self, placeholder_text="Digite algo aqui...")
        self.entry.pack(padx=20, pady=10, fill="x")

        # Botão
        self.button = ctk.CTkButton(self, text="olhe aqui", command=self.clique_botao)
        self.button.pack(padx=20, pady=10)

        # Switch de Tema (Dark/Light)
        self.switch = ctk.CTkSwitch(self, text="Modo Escuro", command=self.alternar_tema)
        self.switch.pack(padx=20, pady=20)
        self.switch.select()

    def clique_botao(self):
        texto = self.entry.get()
        if texto:
            self.label.configure(text=f"Olá, {texto}!")

    def alternar_tema(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

if __name__ == "__main__":
    app = App()
    app.mainloop()