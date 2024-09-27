# models.py

from flask_sqlalchemy import SQLAlchemy

# Instanciamos el objeto SQLAlchemy que se utilizará para interactuar con la base de datos
db = SQLAlchemy()

# Definimos el modelo de datos para las reservas
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único para cada reserva (clave primaria)
    user_name = db.Column(db.String(50), nullable=False)  # Nombre del usuario que realiza la reserva
    court_name = db.Column(db.String(50), nullable=False)  # Nombre de la cancha reservada
    date = db.Column(db.String(20), nullable=False)  # Fecha de la reserva (formato: YYYY-MM-DD)
    time = db.Column(db.String(20), nullable=False)  # Hora de la reserva (formato: HH:MM)

    # Representación en cadena de texto de una reserva para fines de depuración
    def __repr__(self):
        return f'<Reservation {self.user_name} - {self.court_name} on {self.date} at {self.time}>'
