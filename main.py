from src import create_app, db
from flask_migrate import Migrate
from src.model.users import User
from src.model.person import Person
from src.model.address import Address
from src.model.contact import Contact


app = create_app('dev')
Migrate(app, db)

@app.shell_context_processor
def shell_context():
    return dict (
        app=app,
        db=db,
        User=User,
        Person=Person,
        Address=Address,
        Contact=Contact
    )
eapp.run(debug=True)