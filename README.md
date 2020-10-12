# testflask
Test para ejercicio de prueba técnica


## Instalación

```bash
pip install requirements.txt
```

## Configuración

```bash
export FLASK_APP=apps
```
```bash
export APP_SETTINGS="config.DevelopmentConfig"
```
```bash
export APP_SETTINGS="config.TestingConfig"
```

## Configuración de bases de datos, podrá configurar los demás parámetros en config.py
```sql
CREATE DATABASE stock;
```
```sql
CREATE DATABASE inventarios_test;
```
```bash
python manage.py db upgrade
```

## Ejecutar proyecto
```bash
flask run
```

## Ejecutar proyecto
Los ws services están documentados en http://127.0.0.1:5000/docs



