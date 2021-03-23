# finance_credit
Proyecto donde se desarrollo una api rest para manipular solicitudes de credito

Primer paso para conectar la aplicación:
  si usaran algun servidor utilicen el archivo settings/productions.py
  si usaran el servidor local utilicen el archivo settings/local.py
en ambos casos se configura la base de datos

Segundo paso:
  creen un entorno virtual,
  utilicen "pip install -r requirements.txt" para instalar todos los package que utilice en este proyecto
  
Tercer paso:
  en la consola corran los comandos de "python manage.py makemigrations" y "python manage.py migrate" luego de instalar su entorno virtual e instalar todos los requerimientos
  
La aplicación cuenta con varias rutas para acceder a la api, aun esta en modo "dev" por lo que la interfaz de django para hacer peticiones en los serializadores estara activa

http://127.0.0.1:8000/api/v1/client # listado de clientes
http://127.0.0.1:8000/api/v1/client/id # cliente unico
http://127.0.0.1:8000/api/v1/request/ # listado de solicitudes creditarias
http://127.0.0.1:8000/api/v1/request/id # solicitud creditaria unica

los listados cuentan con "GET, POST"
las vistas unicas cuentan con "GET, PUT, DELETE"

no olviden iniciar el servidor en el puerto 8000, en tal caso que no puedan, modifiquen el archivo que simula el consumo de la api "apps/finance_request/api/services.py" 

Cuarto paso:
  creen un super usuario "python manage.py createsuperuser"
  aprovecho el admin de django para poder crear clientes y solicitudes de prueba para manipular la api rest
  http://127.0.0.1:8000/admin
  
Quinto paso:
  en la ruta http://127.0.0.1:8000/client se hace uso de la mayoria de las api, aunque en los servicios esta desarrollado a traves de funciones los metodos mas importantes, solo uso "GET, DELETE y PUT" para manipular los datos en el listado de clientes con sus solicitudes
  
 
 Con esto deberian de poder probar la aplicación, se que el front no es el mejor, utilice como freamwork materialize, queria enfocarme netamente en el backend ya que no contaba con mucho tiempo, hice los metodos de la api atravez de funciones y no clases porque el proyecto es pequeño y en este caso creo que funcionarian mejor ademas que se entiende mejor la logica de lo que sucede realmente con la api que con una clase, intente documentar todo, una disculpa de antemano si se me paso algo...

¡Sin mas nada que comentar, Espero les guste el backend de la app!

