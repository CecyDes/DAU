import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Task:
    def __init__(self, description, category, importance, due_date, due_time):
        self.description = description
        self.category = category
        self.importance = importance
        self.due_date = due_date
        self.due_time = due_time

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestor de Tareas")
        self.tasks = []

        self.create_widgets()  # Crear widgets

    def create_widgets(self):  # Etiquetas y entradas
        tk.Label(self.master, text="Descripción:").grid(row=0, column=0, sticky="w")
        self.description_entry = tk.Entry(self.master, width=30)
        self.description_entry.grid(row=0, column=1, columnspan=2)

        tk.Label(self.master, text="Categoría:").grid(row=1, column=0, sticky="w")
        self.category_entry = tk.Entry(self.master, width=20)
        self.category_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Importancia:").grid(row=2, column=0, sticky="w")
        self.importance_combo = ttk.Combobox(self.master, values=["Baja", "Media", "Alta"])
        self.importance_combo.grid(row=2, column=1)

        tk.Label(self.master, text="Fecha (YYYY-MM-DD):").grid(row=3, column=0, sticky="w")
        self.date_entry = tk.Entry(self.master, width=20)
        self.date_entry.grid(row=3, column=1)

        tk.Label(self.master, text="Hora (HH:MM):").grid(row=4, column=0, sticky="w")
        self.time_entry = tk.Entry(self.master, width=20)
        self.time_entry.grid(row=4, column=1)

        # Botones
        tk.Button(self.master, text="Agregar Tarea", command=self.add_task).grid(row=5, column=0, columnspan=2)
        tk.Button(self.master, text="Mostrar Tareas", command=self.show_tasks).grid(row=5, column=2)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.master, width=50, height=10)
        self.task_listbox.grid(row=6, column=0, columnspan=3)

    def add_task(self):
        description = self.description_entry.get()
        category = self.category_entry.get()
        importance = self.importance_combo.get()
        due_date = self.date_entry.get()
        due_time = self.time_entry.get()

        if not all([description, category, importance, due_date, due_time]):
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            datetime.strptime(due_time, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto.")
            return

        task = Task(description, category, importance, due_date, due_time)
        self.tasks.append(task)
        self.clear_entries()
        messagebox.showinfo("Éxito", "Tarea agregada correctamente.")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task.description} - {task.category} - {task.importance} - {task.due_date} {task.due_time}")

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.importance_combo.set('')
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
