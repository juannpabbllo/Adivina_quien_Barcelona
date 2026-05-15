# Akinator Blaugrana 🔵🔴

Un sistema experto basado en conocimiento diseñado para identificar jugadores históricos y actuales del FC Barcelona. El proyecto utiliza lógica de inteligencia artificial clásica para deducir la identidad de un jugador mediante una serie de preguntas dinámicas.

##  Características
- **Motor de Inferencia:** Implementa encadenamiento hacia adelante (Forward Chaining).
- **Base de Conocimientos Dinámica:** Almacenamiento en formato JSON que permite una fácil expansión.
- **Capacidad de Aprendizaje:** Si el sistema no conoce a un jugador, solicita sus datos y "aprende" en tiempo real para futuras partidas.
- **Interfaz Moderna:** Desarrollado con `CustomTkinter` para una experiencia visual atractiva y fluida.

##  Fundamentos Teóricos

### Teoría de Reglas y Casos
El sistema opera bajo una estructura de **Base de Conocimientos**. 
- **Casos:** Cada entrada en el archivo `base_akinator_fcb.json` representa un caso único con atributos definidos (nacionalidad, posición, zurdo/diestro, etc.).
- **Reglas:** El motor de inferencia traduce estos casos en reglas lógicas condicionales. Si un usuario responde "Sí" a una característica, el sistema activa una regla de filtrado que mantiene solo los casos que cumplen con dicha condición.

### Encadenamiento hacia adelante (Forward Chaining)
El juego utiliza una estrategia de razonamiento que parte de los datos (las respuestas del usuario) para llegar a una conclusión (el jugador). A medida que se recolectan "hechos" a través de las preguntas, el sistema avanza eliminando hipótesis falsas hasta que solo queda un candidato posible.

## 🛠️ Instalación

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/akinator-blaugrana.git](https://github.com/tu-usuario/akinator-blaugrana.git)
