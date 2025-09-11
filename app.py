from flask import Flask
from backend.config import LocalDevelopmentConfig
from backend.model import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore

from backend.celery_factory import celery_init_app

def createApp():
    app = Flask(
        __name__,
        template_folder='./frontend',
        static_folder='./frontend',
        static_url_path='/static/'
    )
    #app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='/static')

    app.config.from_object(LocalDevelopmentConfig)

    db.init_app(app)
    #flask security
    datastore = SQLAlchemyUserDatastore(db, User, Role)

    app.security = Security(app, datastore=datastore, register_blueprint=False)
    app.app_context().push()
    from backend.api import api
    # flask-restful init
    api.init_app(app)
    return app

app = createApp()
import backend.create_initial_data
import backend.router
#print(app.url_map)

celery_app=celery_init_app(app)
from backend import tasks 
from backend import celery_schedule


import os
os.environ["OPENAI_API_KEY"] = "sk-or-v1-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
if (__name__ == '__main__'):
    app.run()
