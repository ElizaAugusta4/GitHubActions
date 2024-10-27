from flask import Flask, request, jsonify
from db import db_session, init_db  # importa a função init_db do database
from models import Item

app = Flask(__name__)

# Chamando init_db para garantir que a tabela é criada
init_db()

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    item = Item(name=data['name'])
    db_session.add(item)
    db_session.commit()
    return jsonify({'id': item.id, 'name': item.name})

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name} for item in items])

if __name__ == "__main__":
    app.run(debug=True)
