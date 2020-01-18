# API Hotel
API de peliculas construidos con DJANGO.

- Construido con Django


## Express Router and Routes

| Route           | HTTP Verb | Description                          |
| --------------- | --------- | ------------------------------------ |
| /top-movie/     | GET       | Obtener listado de peliculas populares   |
| /detail-movie/:id  | GET       | Obtener una pelicula por id           |


## Herramientas utilizadas en este proyecto.
* [Django](https://www.djangoproject.com/)


## Empezando

### Prerrequisitos

- [Git](https://git-scm.com/)
- [Django](https://www.djangoproject.com/) - Django >= 3.0.2


### Developing

1. Ejecutar el comando `pip install -r requirements.txt` para instalar las dependencias.

2. Ejecutar el comando `source env/bin/activate` para encender el entorno virtual.

3. Ejecutar el comando `python3 manage.py runserver` para iniciar el servidor de desarrollo.

4. Abrir el navegador y colocar la siguiente ruta `http://127.0.0.1:8000/top-movie`.

### Deployment

Se utiliza la plataforma como servicio (PaaS), para el despliegue de [API](https://apimovieapp.herokuapp.com) usando HEROKU CLI y sigiendo la guia [guia](https://devcenter.heroku.com/articles/getting-started-with-nodejs#deploy-the-app).

## License

Este proyecto tiene licencia bajo MIT  [LICENSE](LICENSE) para mas detalles abrir el archivo

