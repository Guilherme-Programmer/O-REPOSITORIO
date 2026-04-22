from flask import Flask
import random

app = Flask(__name__)

fatos = [
    "Todos os mamíferos são capazes de saltar, menos os elefantes." 
    "Girafas não têm cordas vocais."
    "A língua de uma baleia-azul pode pesar até 3,6 toneladas, o equivalente ao peso de um elefante médio."
    "As borboletas têm cerca de 12 mil olhos."
]

@app.route("/")
def hello_world():
    return f"""
    <html>
        <head>
            <title>Fatos Curiosos para Curiosos</title>
        </head>
        <body>
        <h1>Fato Aleatório</h1>
        <p>{random.choice(fatos)}</p>
        <p>Aperte F5 para ter um novo fato aleatório</p>
        </body>
    </html>
    
if __name__ == "__main__":
    app run(debug-true)