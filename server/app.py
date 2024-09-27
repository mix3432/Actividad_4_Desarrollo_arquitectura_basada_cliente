from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import re
from models import db, Reservation

# Crear la aplicación Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Función para validar la hora en formato HH:MM
def validate_time_format(time):
    return re.match(r'^\d{2}:\d{2}$', time) is not None

# Función para crear una nueva reserva
def create_reservation(user_name, court_name, date, time):
    if not validate_time_format(time):
        messagebox.showerror("Error de Formato", "Por favor ingrese la hora en el formato HH:MM.")
        return

    with app.app_context():
        new_reservation = Reservation(
            user_name=user_name,
            court_name=court_name,
            date=date,
            time=time
        )
        db.session.add(new_reservation)
        db.session.commit()
        messagebox.showinfo("Éxito", "¡Reserva creada con éxito!")

# Función para cargar y mostrar las reservas existentes
def load_reservations():
    with app.app_context():
        reservations = Reservation.query.all()
        reservations_list.delete(0, tk.END)  # Limpiar la lista antes de añadir nuevas reservas
        for reservation in reservations:
            reservations_list.insert(
                tk.END, 
                f'{reservation.user_name} reservó {reservation.court_name} el {reservation.date} a las {reservation.time}'
            )

# Configuración de la ventana principal de tkinter
root = tk.Tk()
root.title("Reservas de Cancha Deportiva")
root.geometry("400x400")  # Ajusta el tamaño de la ventana (ancho x alto)
root.resizable(False, False)  # Evita que la ventana sea redimensionada

# Crear y colocar los widgets en la ventana
tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky='e', pady=5)
user_name_entry = tk.Entry(root, width=30)
user_name_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Cancha:").grid(row=1, column=0, sticky='e', pady=5)
court_name_entry = tk.Entry(root, width=30)
court_name_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, sticky='e', pady=5)
date_entry = DateEntry(root, date_pattern='yyyy-mm-dd', width=28)  # Ampliar para que coincida con el campo de nombre
date_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Hora (HH:MM):").grid(row=3, column=0, sticky='e', pady=5)
hora_frame = tk.Frame(root)
hora_frame.grid(row=3, column=1, pady=5)

time_entry = tk.Spinbox(hora_frame, from_=0, to=23, format='%02.0f', width=5)  # Spinbox para las horas
time_entry.pack(side='left')
tk.Label(hora_frame, text=":").pack(side='left')  # Etiqueta para el símbolo ":"
minute_entry = tk.Spinbox(hora_frame, from_=0, to=59, format='%02.0f', width=5)  # Spinbox para los minutos
minute_entry.pack(side='left')

def on_reserve():
    time = f"{time_entry.get()}:{minute_entry.get()}"
    create_reservation(
        user_name_entry.get(),
        court_name_entry.get(),
        date_entry.get(),
        time
    )

tk.Button(
    root, text="Reservar", 
    command=on_reserve
).grid(row=4, columnspan=2, pady=10)

reservations_list = tk.Listbox(root, width=50)
reservations_list.grid(row=5, columnspan=2, pady=10)

tk.Button(
    root, text="Cargar Reservas", 
    command=load_reservations
).grid(row=6, columnspan=2, pady=10)

# Ejecutar el bucle principal de tkinter
root.mainloop()
