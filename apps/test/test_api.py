import json
from . import BaseApiTest

class TestApi(BaseApiTest):
    
    def test_asociar_inventario(self):
        payload = json.dumps({
            'producto_id': 1, 
            'existencia': 14
        })
        res = self.app.post('/tiendas/1/inventarios',
            headers={"Content-Type": "application/json"}, 
            data=payload)    
        self.assertEqual(200, res.status_code)
        self.assertIn(b'id', res.data)

    def test_listado_inventario(self):
        res = self.app.get('/tiendas/1/inventarios')    
        self.assertEqual(200, res.status_code)
    
    def test_validar_existencias_esp_cantidad(self):
        res = self.app.get('/tiendas/1/productos/1/existencia?cantidad=5')    
        self.assertEqual(200, res.status_code)
        self.assertIn(b'suficiente', res.data)

    def test_validar_existencias(self):
        res = self.app.get('/tiendas/1/productos/1/existencia')    
        self.assertEqual(200, res.status_code)
        self.assertIn(b'existencia', res.data)
    