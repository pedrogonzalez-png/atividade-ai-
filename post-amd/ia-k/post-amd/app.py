from flask import Flask
from db import db
from routes.amd_routes import amd_routes   

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(amd_routes)

if __name__ == '__main__':
    app.run(debug=True)