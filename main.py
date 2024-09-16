import tkinter as tk
from tkinter import ttk, messagebox
import math
from calculator import Calculator
from history_manager import HistoryManager
from theme_manager import ThemeManager

class EKA:
    def __init__(self, master):
        self.master = master
        self.master.title("EKA - Elektronik Hesap Makinesi")
        self.master.geometry("400x600")

        self.calculator = Calculator()
        self.history_manager = HistoryManager()
        self.theme_manager = ThemeManager()

        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_display = ttk.Entry(self.master, textvariable=self.result_var, justify="right", font=("Arial", 24), state="readonly")
        self.result_display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.operation_var = tk.StringVar()
        self.operation_var.set("Toplama")
        operations = ["Toplama", "Çıkarma", "Çarpma", "Bölme", "Yüzde", "Üs Alma", "Karekök"]
        self.operation_menu = ttk.Combobox(self.master, textvariable=self.operation_var, values=operations, state="readonly")
        self.operation_menu.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '^', '%',
            'sin', 'cos', 'tan', 'log'
        ]

        row_val = 2
        col_val = 0

        for button in buttons:
            cmd = lambda x=button: self.click(x)
            btn = ttk.Button(self.master, text=self.translate_button(button), command=cmd)
            btn.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Yeni özellikler: Sıfırla ve Geri Al düğmeleri
        ttk.Button(self.master, text="Sıfırla", command=self.reset).grid(row=row_val, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(self.master, text="Geri Al", command=self.undo).grid(row=row_val, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)

        row_val += 1
        ttk.Button(self.master, text="Geçmiş", command=self.show_history).grid(row=row_val, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        ttk.Button(self.master, text="Tema Değiştir", command=self.change_theme).grid(row=row_val, column=2, columnspan=2, sticky="nsew", padx=2, pady=2)
        for i in range(row_val + 1):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def translate_button(self, button):
        translations = {
            'C': 'Temizle',
            '√': 'Karekök',
            '^': 'Üs',
            '%': 'Yüzde',
            'sin': 'Sinüs',
            'cos': 'Kosinüs',
            'tan': 'Tanjant',
            'log': 'Logaritma'
        }
        return translations.get(button, button)

    def click(self, key):
        if key == '=':
            result = self.calculator.calculate(self.result_var.get())
            self.result_var.set(result)
            self.history_manager.add_to_history(f"{self.result_var.get()} = {result}")
        elif key == 'C':
            self.reset()
        else:
            current = self.result_var.get()
            if current == "0" or current == "Hata":
                self.result_var.set(key)
            else:
                self.result_var.set(current + key)

    def reset(self):
        self.result_var.set("0")

    def undo(self):
        current = self.result_var.get()
        if len(current) > 1:
            self.result_var.set(current[:-1])
        else:
            self.result_var.set("0")

    def show_history(self):
        history = self.history_manager.get_history()
        history_window = tk.Toplevel(self.master)
        history_window.title("Hesaplama Geçmişi")
        
        for item in history:
            ttk.Label(history_window, text=item).pack(padx=10, pady=5)

    def change_theme(self):
        self.theme_manager.next_theme()
        self.apply_theme()

    def apply_theme(self):
        theme = self.theme_manager.get_current_theme()
        self.master.configure(bg=theme['bg'])
        style = ttk.Style()
        style.configure('TButton', background=theme['button_bg'], foreground=theme['button_fg'])
        style.configure('TEntry', fieldbackground=theme['entry_bg'], foreground=theme['entry_fg'])
        style.map('TButton',
                  background=[('active', theme['button_active_bg'])],
                  foreground=[('active', theme['button_active_fg'])])

if __name__ == "__main__":
    root = tk.Tk()
    app = EKA(root)
    root.mainloop()
