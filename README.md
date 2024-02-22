# Chat en Python

## Planteamiento

### ¿En qué consiste?

La prueba consistiría en realizar un chat entre dos PC usando Python en una arquitectura clientes/servidor.

Script a) - Servidor

Script b) - Clientes

El objetivo es que 2 clientes se conecten al servidor, y a partir de ahí, ambos puedan intercambiarse mensajes.

![Connection picture](./media/image.png)

Todos los mensajes, los debes guardar en un log de mensajes.

Los mensajes a enviar deben ser de forma asíncrona (enviar mensajes sin necesidad de una recepción previa).

### Puntos Clave

- Buenas prácticas de programación.
- Control de errores
- Código comentado (inglés).
- Estructura de código (estructuración de clases, etc).
- Sistema dockerizado (separar docker servidor y docker cliente).

## Desarrollo

Para comenzar se ha realizado el [servidor](./server/Server.py), donde ser administra las conexiones de los usuarios, reenvia los mensajes a los clientes y guarda los mensajes recibidos en el archivo llamado ***chat_history.log***.

El siguiente paso fue crear el [cliente](./client/Client.py), que es capaz de recibir y enviar mensajes de forma asíncrona. Para solucionar este problema se usa la clase **ThreadPoolExecutor**, que permite utilizar diferentes hilos para todas las acciones y conseguir recibir y/o enviar mensajes sin tener que esperar a que termine otro proceso.

Para terminar, se ha creado un archivo ***main.py*** para cada servicio, de cara a poder parametrizarlo a la hora de elegir la dirección IP del servidor, como el puerto que utilice.

## Bibiografía

- [Documentación Python Sockets](https://docs.python.org/es/3/howto/sockets.html)
- [Libro Python Avanzado](https://www.amazon.es/Python-avanzado-en-fin-semana/dp/B08XLGJQQG/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=)
- [Documentación Python Concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor)
- [Video explicando ThreadPoolExecutor](https://www.youtube.com/watch?v=2Koubj0fF9U)
