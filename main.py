from src import create_app, db
from flask_migrate import Migrate
from src.model.users import User
from src.model.person import Person
from src.model.address import Address
from src.model.contact import Contact
from src.model.system import System
from src.model.sytemPermission import SystemPermission
from src.model.profilePermission import ProfilePermission
from src.model.profileSystem import ProfileSystem
from src.model.userProfileSystem import UserProfileSystem


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
        Contact=Contact,

        System=System,
        SystemPermission=SystemPermission,
        ProfilePermission=ProfilePermission,
        ProfileSystem=ProfileSystem,
        UserProfileSystem=UserProfileSystem,
    )

if __name__ == '__main__':
    
    app.run(debug=True)