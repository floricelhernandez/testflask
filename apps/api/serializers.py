from apps import api_router as api
from flask_restplus import  fields

inventario_model = api.model('Stock', {
    'producto_id': fields.Integer,
    'existencia': fields.Integer
})

suficiencia_model = api.model('Suficiencia', {
    'cantidad': fields.Integer
})
