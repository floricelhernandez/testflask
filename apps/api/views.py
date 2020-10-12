import json
import asyncio
import threading
from flask import request, abort
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from .models import Tienda, Stock, Producto
from .serializers import inventario_model, suficiencia_model
from apps import api_router as api
from apps import db

@api.response(200, 'OK')
@api.response(500, 'Operación con errores, no completado')
class ListaTiendasApi(Resource):
    def get(self):
        """
        Lista todas las tiendas
        """
        try:
            tiendas=Tienda.query.all()
            return  [t.serialize() for t in tiendas]
        except Exception as e:
	           abort(500, str(e))


@api.response(200, 'OK')
@api.response(500, 'Operación con errores, no completado')
class ListaProductosApi(Resource):
    def get(self):
        """
        Lista todos los productos
        """
        try:
            tiendas=Tienda.query.all()
            return  [t.serialize() for t in tiendas]
        except Exception as e:
	           abort(500, str(e))


@api.response(200, 'OK')
@api.response(400, 'Datos no válidos en la petición.')
@api.response(404, 'Objeto no encontrado')
@api.response(500, 'Operación con errores, no completado')
class ListaInventarioApi(Resource):
    def get_tienda(self, pk):
        return Tienda.query.get_or_404(pk, description='No se ha encontrado una tienda con id {}'.format(pk))

    def get(self, tienda_id):
        """
        Obtiene la lista de los inventarios de una tienda específica
        """

        tienda = self.get_tienda(tienda_id)
        try:
            stocks=Stock.query.filter_by(tienda_id=tienda.id).all()
            return  [s.serialize() for s in stocks]
        except Exception as e:
	           abort(500, str(e))

    @api.response(201, 'Inventario asociado exitosamente.')
    @api.expect(inventario_model)
    def post(self, tienda_id):
        """
        Agrega un ítem al inventario de una tienda específica
        """

        tienda = self.get_tienda(tienda_id)
        stock = Stock(**request.json)
        stock.tienda_id = tienda.id
        try:
            db.session.add(stock)
            db.session.commit()
            return stock.serialize()
        except IntegrityError:
            abort(400, 'Datos no válidos')
        except Exception:
            abort(500, "Ha ocurrido un error")


@api.response(200, 'OK')
@api.response(400, 'Datos no válidos en la petición.')
@api.response(404, 'Objeto no encontrado')
@api.response(500, 'Operación con errores, no completado')
class ValidadorInventarioApi(Resource):
    def get_tienda(self, pk):
        return Tienda.query.get_or_404(
            pk, 
            description='No se ha encontrado una tienda con id {}'.format(pk)
            )

    def get_producto(self, pk):
        return Producto.query.get_or_404(
            pk, 
            description='No se ha encontrado un producto con id {}'.format(pk)
            )

    async def validar(self, tienda_id, producto_id, cantidad):
        try:
            validacion = {}
            
            
            tienda = self.get_tienda(tienda_id)
            producto = self.get_producto(producto_id)

            stock=Stock.query.filter_by(tienda_id=tienda.id, producto_id=producto.id).first()
            
            if stock is None: # Si no se encuentran registros con los datos proporcionados, devolver status 404
                abort(404, 
                    "No se ha encontrado un stock para {} en la tienda {}".
                    format(producto.nombre, tienda.nombre))
            else:
                if cantidad is None and stock.existencia > 0: # Si no se provee cantidad a calcular y hay stock, indicar que hay suficiente
                    validacion['suficiente']=True 
                else:
                    try:
                        cantidad = int(cantidad)
                    except Exception:
                        abort(400, "Cantidad debe ser un entero")
                    if cantidad <= stock.existencia: # Si el stock es mayor o igual a la cantidad solicitada a evaluar, indicar que hay suficiente
                        validacion['suficiente']=True
                    else: # Si el stock es menor que la cantidad solicitada a evaluar, indicar que no hay suficiente
                        validacion['suficiente']=False
                validacion['existencia'] = stock.existencia
            return validacion
        except Exception as e:
	        abort(500, str(e))
      
    @api.doc(params={'cantidad': {'description':'Cantidad a validar', 'type': 'int'}})
    def get(self, tienda_id, producto_id):
        """
        Valida si hay suficiente inventario de un producto específico para una tienda específica
        """
        cantidad = request.args.get('cantidad')
        result = asyncio.run(self.validar(tienda_id, producto_id, cantidad))
        
        return result
        
        


