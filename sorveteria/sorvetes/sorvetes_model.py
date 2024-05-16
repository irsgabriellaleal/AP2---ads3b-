from config import db

class Sorvete(db.Model):
    id_sorvete = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer)

    def __init__(self, sabor, categoria, preco, estoque):
        self.sabor = sabor
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

    def to_dict(self):
        return {'id': self.id_sorvete,
                'sabor': self.sabor,
                'categoria': self.categoria,
                'preco': self.preco,
                'estoque': self.estoque}
    
class Categoria(db.Model):
    id_categoria = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

    def __init__(self, nome):
        self.nome = nome

    def to_dict(self):
        return {'id': self.id_categoria,
                'nome': self.nome}

class SorveteriaNaoEncontrada(Exception):
    pass

def sorvete_id(id_sorvete):
    sorvete = Sorvete.query.get(id_sorvete)
    if not sorvete:
        raise SorveteriaNaoEncontrada
    return sorvete.to_dict()

def listar_sorvetes():
    sorvetes = Sorvete.query.all()
    return [sorvete.to_dict() for sorvete in sorvetes]

def adicionar_sorvete(sorvete_data):
    novo_sorvete = Sorvete(sabor = sorvete_data['sabor'],
                           categoria = sorvete_data['categoria'],
                           preco = sorvete_data['preco'],
                           estoque = sorvete_data['estoque'])
    db.session.add(novo_sorvete)
    db.session.commit()

def atualizar_sorvete(id_sorvete, novos_dados):
    sorvete = Sorvete.query.get(id_sorvete)
    if not sorvete:
        raise SorveteriaNaoEncontrada
    sorvete.sabor = novos_dados['sabor']
    sorvete.categoria = novos_dados['categoria']
    sorvete.preco = novos_dados['preco']
    sorvete.estoque = novos_dados['estoque']
    db.session.commit()

def excluir_sorvete(id_sorvete):
    sorvete = Sorvete.query.get(id_sorvete)
    if not sorvete:
        raise SorveteriaNaoEncontrada
    db.session.delete(sorvete)
    db.session.commit()
