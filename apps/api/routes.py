from apps import api_router
from .views import ListaTiendasApi, ListaInventarioApi, ValidadorInventarioApi

ns_tiendas = api_router.namespace(
    'tiendas',
    description='Operaciones sobre tiendas') # Generando un espacio de nombres para 'tiendas'

ns_tiendas.add_resource(ListaTiendasApi, '/') #Recurso: Listar tiendas
ns_tiendas.add_resource(ListaInventarioApi, '/<int:tienda_id>/inventarios') #Recurso: Listar y crear inventario
ns_tiendas.add_resource(ValidadorInventarioApi, '/<int:tienda_id>/productos/<int:producto_id>/existencia') #Recurso: Validar stock
