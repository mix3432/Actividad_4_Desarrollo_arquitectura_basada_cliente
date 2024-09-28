# models.py

from flask_sqlalchemy import SQLAlchemy

# Instanciamos el objeto SQLAlchemy que se utilizará para interactuar con la base de datos
db = SQLAlchemy()


# Definimos el modelo de datos para las reservas
class Reservation(db.Model):
    """ 
    Modelo de datos para las reservas de canchas.
    """

    # ID único para cada reserva (clave primaria)
    id = db.Column(
        db.Integer, primary_key=True)
    # Nombre del usuario que realiza la reserva
    user_name = db.Column(db.String(50), nullable=False)
    # Nombre de la cancha reservada
    court_name = db.Column(db.String(50), nullable=False)
    # Fecha de la reserva (formato: YYYY-MM-DD)
    date = db.Column(db.String(20), nullable=False)
    # Hora de la reserva (formato: HH:MM)
    time = db.Column(db.String(20), nullable=False)

    # Representación en cadena de texto de una reserva para fines de depuración
    def __repr__(self):
        return f'<Reservation {self.user_name} - {self.court_name} on {self.date} at {self.time}>'
