# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from monitorar.monitoramento_service import listar_mudancas

monitoramento_db.init()

monitoramento_app = Flask(__name__)

@monitoramento_app.route('/')
def service_listar():
    return jsonify(listar_mudancas())


if __name__ == '__main__':
    monitoramento_app.run(host='localhost', port=5005)