import os
from apps import db, app
from  unittest import TestCase
from apps.api.models import Tienda, Producto, Stock


class BaseApiTest(TestCase):
    
    def setUp(self):
        app.config.from_object(os.environ['APP_SETTINGS_TEST'])
        self.app = app.test_client()
        tienda1 = Tienda('La mejor','La esquina #86')
        db.session.add(tienda1)

        producto1 = Producto('Jugo de sabor')
        db.session.add(producto1)

        stock1 = Stock(1,10)
        stock1.tienda_id = 1
        db.session.add(stock1)

        db.create_all()
        db.session.commit()

    def tearDown(self):
        
        # Elimina todas las tablas de la base de datos
        db.session.remove()
        db.drop_all()
