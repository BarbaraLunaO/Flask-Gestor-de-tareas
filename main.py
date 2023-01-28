from flask import Flask, render_template, request, redirect, url_for

import db
from models import Tarea

app = Flask(__name__) #En app se encuentra nuestro servidor web de Flask

@app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    for i in todas_las_tareas:
        print(i)
    porcentaje_tareas = progreso()
    return render_template("index2.html", lista_de_tareas=todas_las_tareas,p= porcentaje_tareas)

@app.route("/crear-tarea", methods=["POST"])
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False, categoria=request.form["contenido_categoria"])
    print("bg_"+request.form["contenido_categoria"])
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

def progreso():
    tareas_hechas = db.session.query(Tarea).filter_by(hecha=True).count()
    tareas_totales = db.session.query(Tarea).count()
    if tareas_totales == 0:
        porcentaje_tareas = 0
    else:
        porcentaje_tareas = int((tareas_hechas * 100) / tareas_totales)
    print("{} tareas hechas ---> {}%".format(tareas_hechas, tareas_totales))
    return porcentaje_tareas

@app.route("/editar-tarea/<id>")
def editarTarea():
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()



if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug = True)