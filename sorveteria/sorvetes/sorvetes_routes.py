#from config import db
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .sorvetes_model import SorveteriaNaoEncontrada, listar_sorvetes, sorvete_id, adicionar_sorvete, atualizar_sorvete, excluir_sorvete

sorvetes_blueprint = Blueprint('sorvetes', __name__)

@sorvetes_blueprint.route('/', methods=['GET'])
def getIndex():
    return "Meu index"

@sorvetes_blueprint.route('/sorvetes', methods=['GET'])
def get_sorvetes():
    sorvetes = listar_sorvetes()
    return render_template("sorveteria.html", sorvetes=sorvetes)

@sorvetes_blueprint.route('/sorvetes/<int:id_sorvete>', methods=['GET'])
def get_sorvete(id_sorvete):
    try:
        sorvete = sorvete_id(id_sorvete)
        return render_template('sorveteria_id.html', sorvete=sorvete)
    except SorveteriaNaoEncontrada:
        return jsonify({'message': 'Sorvete não encontrado'}), 404
  
@sorvetes_blueprint.route('/sorvetes/adicionar', methods=['GET'])
def adicionar_sorvete_page():
    return render_template('criarSorveteria.html')

@sorvetes_blueprint.route('/sorvetes', methods=['POST'])
def create_sorvete():
    sabor = request.form['sabor']
    categoria = request.form['categoria']
    preco = request.form['preco']
    estoque = request.form['estoque']
    novo_sorvete = {'sabor': sabor,
                    'categoria': categoria,
                    'preco': preco,
                    'estoque': estoque}
    adicionar_sorvete(novo_sorvete)
    return redirect(url_for('sorvetes.get_sorvetes'))

@sorvetes_blueprint.route('/sorvetes/<int:id_sorvete>/editar', methods=['GET'])
def editar_sorvete_page(id_sorvete):
    try:
        sorvete = sorvete_id(id_sorvete)
        return render_template('sorveteria_update.html', sorvete=sorvete)
    except SorveteriaNaoEncontrada:
        return jsonify({'message': 'Sorvete não encontrado'}), 404

@sorvetes_blueprint.route('/sorvetes/<int:id_sorvete>', methods=['PUT',"POST"])
def update_sorvete(id_sorvete):
    print("Dados recebidos no formulário:", request.form)
    try:
        sabor = request.form['sabor']
        categoria = request.form['categoria']
        preco = request.form['preco']
        estoque = request.form['estoque']
        novos_dados = { 'sabor':sabor ,
                        'categoria':categoria,
                         'preco':preco,
                         'estoque':estoque
                     }
        atualizar_sorvete(id_sorvete,novos_dados)
        return redirect(url_for('sorvetes.get_sorvete', id_sorvete=id_sorvete))
    except SorveteriaNaoEncontrada:
        return jsonify({'message': 'Sorvete não encontrado'}), 404
   
@sorvetes_blueprint.route('/sorvetes/delete/<int:id_sorvete>', methods=['DELETE','POST'])
def delete_sorvete(id_sorvete):
    try:
        excluir_sorvete(id_sorvete)
        return redirect(url_for('sorvetes.get_sorvetes'))
    except SorveteriaNaoEncontrada:
        return jsonify({'message': 'Sorvete não encontrado'}), 404
