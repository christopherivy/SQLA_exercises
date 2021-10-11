from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!
class Pet(db.Model):
    """ Pet. """
    __tablename__ = 'pets'

        # this is creating a col for the table
    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)
        # this is creating a col for the table
    name = db.Column(db.String(50),
        nullable=False,
        unique=True)

        # this is creating a col for the table
    species = db.Column(db.String(30), nullable=True)

        # this is creating a col for the table
    hunger = db.Column(db.Integer, nullable=False, default=20)


# another section
    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"


    def introduction(self):
        return f"Hi, I am {self.name} the {self.species}"

    # def greet(self):
    #     return f"I'm {self.name} the {self.species}"

    def laugh(self):
        return f"HAHA, I'm the {self.name} laughing at the {self.species}"
    
    def feed(self, amt=20):
        """Update hunger based off of amt """
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)



""" 
                                INSERTS

In ipython I did this:
single insert
        jimi = Pet(name='Jimi',  species='cat')
        rondo = Pet(name='Rondo', species='cat')
        db.session.add(jimi)
        db.session.add(rondo)
        db.session.commit()

                                MULTIPLE INSERTS

In ipython I did this:
name = ['jojo', 'jim', 'willi', 'david']
species = ['horse', 'cow', 'beaver', 'dog']

zip(names, species)

[Pet(name=n, species=s) for n,s in zip(name, species)]

pets[0].name
        'jojo'


If you try to add another pet and its a duplicate it will give you an
error(rollback errer). Then if you try to add another pet after the duplicate 
it will still not add it due to the previous error.

to fix:
        db.session.rollback()
        db.session.add(fish)
        then pet can be added.

                                CHANGING VALUES

To change a name: (in ipython)
        jimi.name = 'Jimi John'
        db.session.add(jimi)
        db.session.commit() (you will see and update)
 

                                QUERYING


Pet.query.all() is doing this:
    SELECT * FROM pets;

Pet.query.get(1) 
    SELECT * FROM pets WHERE id=1;
 """
