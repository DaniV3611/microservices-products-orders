# Microservicios de Productos y Pedidos con NGINX, Docker y Bases de Datos

Este proyecto implementa un sistema de microservicios utilizando Docker para contenerizar los servicios de productos y pedidos, con NGINX actuando como proxy inverso. Los servicios están conectados a bases de datos MongoDB (para productos) y PostgreSQL (para pedidos). Los microservicios están diseñados para ser escalables y accesibles a través de un solo punto de entrada, NGINX.

## Arquitectura

### Servicio de Productos (product-service):

- Hecho en Node.js con Express.js.
- Se conecta a MongoDB para almacenar la información de productos.
- Los productos están disponibles a través de un endpoint REST.

### Servicio de Pedidos (order-service):

- Hecho en Python con FastAPI.
- Se conecta a PostgreSQL para almacenar los pedidos.
- Los pedidos se pueden consultar a través de un endpoint REST.

### NGINX:

- Actúa como proxy inverso para redirigir las solicitudes a los microservicios correspondientes.
- Configurado para enrutar las solicitudes de `/products` al servicio de productos y `/orders` al servicio de pedidos.

### Bases de Datos:

- MongoDB para almacenar productos.
- PostgreSQL para almacenar pedidos.

### Docker:

- Todos los servicios se ejecutan en contenedores Docker.
- Se usa Docker Compose para orquestar los contenedores y facilitar su gestión.

## Requisitos Previos

Docker y Docker Compose deben estar instalados en tu máquina.

## Endpoints

### 1. Servicio de Productos

**URL**: `/products`

**Método**: GET

**Descripción**: Obtiene la lista completa de productos.

**Respuesta Exitosa (200)**:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 1500
  },
  {
    "id": 2,
    "name": "Phone",
    "price": 800
  }
]
```

**URL**: `/products/{productId}`

**Método**: GET

**Descripción**: Obtiene un producto específico por su productId.

**Respuesta Exitosa (200)**:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 1500
}
```

**Respuesta de Error (404)**:

```json
{
  "error": "Product not found"
}
```

### 2. Servicio de Pedidos

**URL**: `/orders/`

**Método**: GET

**Descripción**: Obtiene la lista completa de pedidos.

**Respuesta Exitosa (200)**:

```json
[
  {
    "product_id": "680eda46826b9fbecd7ba3d9",
    "quantity": 1,
    "id": 1
  }
]
```

**URL**: `/orders/`

**Método**: POST

**Descripción**: Crea un nuevo pedido.

**Cuerpo de la Solicitud**:

```json
{
  "product_id": "680eda46826b9fbecd7ba3d9",
  "quantity": 1
}
```

**Respuesta Exitosa (200)**:

```json
{
  "product_id": "680eda46826b9fbecd7ba3d9",
  "quantity": 1,
  "id": 1
}
```

**Respuesta de Error (404)**:

```json
{
  "detail": "Product not found"
}
```

## Arquitectura y Detalles Técnicos

### NGINX como Proxy Inverso

NGINX está configurado para enrutar las solicitudes de:

- `/products` a product-service.
- `/orders` a order-service.

NGINX asegura que las APIs de productos y pedidos no sean accesibles directamente a través de sus puertos internos. Los puertos expuestos de los servicios product-service y order-service han sido deshabilitados para evitar accesos directos desde el exterior.

### Docker y Docker Compose

- Docker Compose se utiliza para orquestar y gestionar los contenedores.
- Cada servicio (product-service, order-service, mongo, postgres, nginx) se ejecuta en un contenedor independiente.
- El archivo [`docker-compose.yml`](docker-compose.yml) gestiona las redes internas entre los servicios para asegurar la comunicación entre ellos.

### Bases de Datos

- **MongoDB**: Utilizado para almacenar productos. Se configura con un contenedor dedicado.
- **PostgreSQL**: Utilizado para almacenar los pedidos. También está contenido en su propio contenedor.

### Redes

- Todos los servicios se comunican a través de una red de Docker llamada `app-network`.
- NGINX está configurado para redirigir las solicitudes solo hacia los servicios que están en esta red, garantizando que el tráfico no se desvíe hacia fuera de la red de Docker.

## Instrucciones para Ejecutar el Proyecto

1. **Clona este repositorio**:

```bash
git clone https://github.com/tu-usuario/mi-proyecto-microservicios.git
cd mi-proyecto-microservicios
```

2. **Construir y levantar los contenedores**:

Si aún no has construido los contenedores, puedes hacerlo ejecutando el siguiente comando:

```bash
docker-compose up --build
```

Esto construirá los servicios y levantará los contenedores de Docker.

3. **Acceder a las APIs**:

Una vez que todo esté corriendo, podrás acceder a los servicios a través de las siguientes URLs:

- http://localhost/products (Lista de productos)
- http://localhost/products/{productId} (Detalle de un producto)
- http://localhost/orders (Lista de pedidos)

4. **Detener los contenedores**:

Para detener los contenedores, simplemente ejecuta:

```bash
docker-compose down
```

## Mejoras Futuras

- Implementar autenticación y autorización en los microservicios.
- Configurar escala horizontal para los servicios de productos y pedidos.
- Implementar logging y monitoreo para los microservicios y NGINX.
- Utilizar un orquestador de contenedores como Kubernetes para manejar la alta disponibilidad y la distribución de contenedores.
