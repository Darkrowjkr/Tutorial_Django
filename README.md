# Tutorial_Django (Ubuntu/Debian)
Tutorial de Django con SQLite
###INSTALACION###
Debe tenerse instalado el python en el ordenador con una version mayor a 3.0.0, aqui el comando:
 --$ sudo apt-get install python3
 --$ sudo apt-get update
Para comprobar que si se instaló escribimos en la terminal:
 --$ python3 --version
Habiendo comprobado que lo tenemos instalamos el pip para mas rapidez y facilidad en descargar lo que necesitamos:
 --$ sudo apt install python3-pip
Ahora ya teniendo python y pip, instalamos el framework Django con el comando:
 --$ python3 pip -m install django
Es todo lo necesario de instalar para usarlo.

###USO###
Abrimos terminal en la carpeta:
 --$ cd nombre_carpeta
Activamos el servidor en 127.0.0.1:8000 (default):
 --$ python3 manage.py runserver
Abrimos la direccion en el navegador y ahi puede ingresar a 'polls' o 'admin'.
