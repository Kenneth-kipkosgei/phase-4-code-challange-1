from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///superheroes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# Import models and initialize db
from models import db, Hero, Power, HeroPower

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)

# Routes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(only=('id', 'name', 'super_name')) for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    
    return jsonify(hero.to_dict(only=('id', 'name', 'super_name', 'hero_powers')))

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict(only=('id', 'name', 'description')) for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    
    return jsonify(power.to_dict(only=('id', 'name', 'description')))

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404
    
    data = request.get_json()
    if 'description' in data:
        power.description = data['description']
    
    try:
        db.session.commit()
        return jsonify(power.to_dict(only=('id', 'name', 'description')))
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['validation errors']}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    try:
        hero_power = HeroPower(
            strength=data.get('strength'),
            power_id=data.get('power_id'),
            hero_id=data.get('hero_id')
        )
        
        db.session.add(hero_power)
        db.session.commit()
        
        return jsonify(hero_power.to_dict(only=('id', 'hero_id', 'power_id', 'strength', 'hero', 'power'))), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['validation errors']}), 400

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        msg = Message(
            'Test Email from Superheroes API',
            sender=app.config['MAIL_USERNAME'],
            recipients=['test@example.com']
        )
        msg.body = 'This is a test email from the Superheroes API!'
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'error': 'Failed to send email'}), 500

if __name__ == '__main__':
    app.run(debug=True)