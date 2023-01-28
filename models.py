import db
from sqlalchemy import Column, Integer, String, Boolean


class Tarea(db.Base):
    __tablename__ = "tarea"
    __table__args__ = {'sqlite_autoincrement': True}
    id_tarea = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    categoria = Column(String, nullable=False)

    def __init__(self, contenido, hecha, categoria):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria

    def __str__(self):
        return "Tarea {} -> {} -> {} {}".format(self.id_tarea, self.contenido, self.hecha, self.categoria)

