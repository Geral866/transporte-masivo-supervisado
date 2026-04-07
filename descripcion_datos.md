# Descripción de los datos – Transporte masivo

## Fuentes reales propuestas
- **API de tránsito municipal**: proporciona datos en tiempo real de congestión vehicular (niveles 1-3) y accidentes.
- **Registros históricos del sistema de transporte masivo**: reportes diarios de retrasos en estaciones y rutas.
- **Datos climáticos históricos**: registros de lluvia, niebla o tormentas (variables binarias).

## Justificación del dataset sintético
Dado que no fue posible acceder a las fuentes reales por restricciones de disponibilidad o privacidad, se construyó un dataset de muestra que refleja las relaciones típicas entre hora del día, nivel de tráfico, condiciones climáticas y la ocurrencia de retrasos.

## Estructura del dataset (`transporte.csv`)
| Columna  | Tipo    | Rango / Valores           | Descripción                               |
|----------|---------|---------------------------|-------------------------------------------|
| hora     | int     | 800 – 2200                | Hora del día en formato HHMM              |
| trafico  | int     | 1 (bajo), 2 (medio), 3 (alto) | Nivel de congestión vehicular          |
| clima    | int     | 0 (bueno), 1 (lluvia)     | Condición climática (binaria)             |
| retraso  | int     | 0 (sin), 1 (con)          | Variable objetivo: retraso en el servicio |

## Volumen de datos
El dataset actual contiene 12 registros de ejemplo, suficientes para demostrar el flujo de trabajo de aprendizaje supervisado. En un entorno real se requerirían miles de registros.

## Relaciones esperadas
- A mayor tráfico (3) y clima lluvioso (1), mayor probabilidad de retraso.
- Horas pico (800, 1700-1900) tienden a más retrasos.
- El árbol de decisión capturará estas reglas de forma interpretable.