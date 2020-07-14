![alt text](https://github.com/miriamvelloso/Chat-Sentiment-Analysis-Service/blob/master/images/images.png)

## Project: Chat-Sentiment-Analysis-Service

# Introducción:

En este proyecto se creará una API para almacenar mensajes de chat y usuarios en una base de datos de Mongodb. Después analizaremos el sentimiento de los chats como Positivo, Negativo o Neutral. Finalmente, recomendaremos los tres mejores amigos a un usuario en base a la similitud de sentimientos. A continuación encontrará los detalles del proyecto.

En este archivo, hemos creado una API en Flask. Estos son los puntos finales de la API:

**Endpoints:(create.py)**

1. Crea usuarios y guarda en la base de datos de Mongodb: `("/user/create/")`

2. Crea chats y guarda en la base de datos de Mongodb: `("/chat/create/")`

3.  Crear usuarios para un chat:  `("/chat//adduser/")`

4. Añade mensajes a los chats : `("/chat//user//addmessage/")`

**Sentimental analysis `(sentimental.py)`**

Se ha realizado un analisis de sentimientos para los mensajes de un chat especifico. `("/chat//list")`
Para el analisis del sentimiento de los mensajes en el chat se han clasificado en **mayormente positivos** o **mayormente negativos** y mostrar los detalles, usando el paquete de análisis de sentimiento NLTK. `("/chat//sentimiento")`


**Recommended Analysis**

Esta sección es para recomendar al top tres de amigos de un usuario en base a la similitud de sentimientos.

Recomendar amigos usando un sistema de recomendación con análisis de PNL. `("/usuario//recomendar")`



