import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox

class BlocoDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloco de Notas")
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        # Barra de menu
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # Menu Arquivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Novo", command=self.novo_arquivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)
        self.file_menu.add_command(label="Salvar", command=self.salvar_arquivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=root.quit)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)

    def novo_arquivo(self):
        self.text_area.delete(1.0, tk.END)

    def abrir_arquivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)

    def salvar_arquivo(self):
        content = self.text_area.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Salvar", "Arquivo salvo com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlocoDeNotas(root)
    root.mainloop()
