from app import app, db
from models import Hero, Power, HeroPower

def seed_data():
    with app.app_context():
        # Clear existing data
        HeroPower.query.delete()
        Hero.query.delete()
        Power.query.delete()
        
        # Create heroes
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra")
        ]
        
        # Create powers
        powers = [
            Power(name="super strength", description="gives the wielder super-human strengths"),
            Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
            Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
            Power(name="elasticity", description="can stretch the human body to extreme lengths")
        ]
        
        # Add to database
        for hero in heroes:
            db.session.add(hero)
        for power in powers:
            db.session.add(power)
        
        db.session.commit()
        
        # Create hero powers
        hero_powers = [
            HeroPower(strength="Strong", hero_id=1, power_id=2),
            HeroPower(strength="Average", hero_id=2, power_id=1),
            HeroPower(strength="Weak", hero_id=3, power_id=3),
            HeroPower(strength="Strong", hero_id=4, power_id=2),
            HeroPower(strength="Average", hero_id=5, power_id=4)
        ]
        
        for hero_power in hero_powers:
            db.session.add(hero_power)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()