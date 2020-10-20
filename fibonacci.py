import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():
    anterior = 0
    proximo = 1
    i = 0
    resposta = '1, '

    while(i <= 50):
        proximo = proximo + anterior
        anterior = proximo - anterior
        i += 1

        if(proximo == 0):
            proximo = proximo + 1    

        resposta+= str(proximo) + ", "


    return resposta


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
