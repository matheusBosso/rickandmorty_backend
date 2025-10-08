from flask import Flask
from src.models import db
from config.settings import DATABASE_URI
from src.routes.characters_route import characters_bp

app = Flask(__name__) # inicializando o Flask
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI # configurando o banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # inicializando o banco de dados com o Flask

app.register_blueprint(characters_bp, url_prefix = '/characters')  # registrando o blueprint de personagens

if __name__ == '__main__':
    app.run(debug = True)  # executando o servidor Flask em modo de debbug automaticamente