from models.amd_models import Amd
from db import db
import json
from flask import make_response

def create_amd(amd_data):

    novo_amd = Amd(
        nome=amd_data['nome'],
        categoria=amd_data['categoria'],
        preco=amd_data['preco']
    )

    db.session.add(novo_amd)
    db.session.commit()

    response = make_response(
        json.dumps({
            'mensagem': 'Produto AMD cadastrado com sucesso.',
            'amd': novo_amd.json()
        }, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response