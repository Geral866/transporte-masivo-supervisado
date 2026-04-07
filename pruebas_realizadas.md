# Pruebas realizadas – Modelo de árbol de decisión para transporte masivo

## Salida completa de la ejecución
PS C:...\transporte-masivo-supervisado> py modelo.py
✓ Creando dataset de ejemplo...
✓ Dataset guardado como transporte.csv

--- Dataset ---
hora trafico clima retraso
0 800 1 0 0
1 815 2 1 1
2 830 3 0 0
3 845 2 1 1
4 900 1 1 0
Total registros: 12

✓ Entrenamiento: 8 registros
✓ Prueba: 4 registros
✓ Modelo entrenado (árbol de decisión con max_depth=3)

========================================
RESULTADOS DE EVALUACIÓN
========================================
Precisión (accuracy) en test: 1.00 (100.0%)

Matriz de confusión:
[[2 0]
[0 2]]

Reporte de clasificación:
precision recall f1-score support

Sin retraso 1.00 1.00 1.00 2
Con retraso 1.00 1.00 1.00 2

accuracy 1.00 4
macro avg 1.00 1.00 1.00 4
weighted avg 1.00 1.00 1.00 4

Validación cruzada (5 folds): [0.66666667 0.66666667 1. 1. 1. ]
Precisión promedio CV: 0.87 (+/- 0.16)

========================================
PREDICCIONES PARA NUEVOS CASOS
========================================
Hora=930, Tráfico=3, Clima=1 → CON retraso (probabilidad: 1.00)
Hora=800, Tráfico=1, Clima=0 → SIN retraso (probabilidad: 1.00)
Hora=1800, Tráfico=3, Clima=0 → SIN retraso (probabilidad: 0.50)

✓ Árbol de decisión guardado como 'arbol_decision.png'
✓ Modelo guardado como 'modelo_retrasos.pkl'

## Interpretación de los resultados

- **Precisión en test**: 100% (4 casos acertados). Este valor perfecto se debe al tamaño muy pequeño del conjunto de prueba; con más datos el rendimiento sería más realista.
- **Matriz de confusión**: Sin errores (2 verdaderos negativos, 2 verdaderos positivos).
- **Validación cruzada (5 folds)**: Precisión promedio 0.87 (±0.16), mostrando cierta variabilidad por la cantidad limitada de datos.
- **Predicciones destacadas**:
  - (930, tráfico=3, clima=1) → Con retraso (probabilidad 1.00): coherente con alta congestión y lluvia.
  - (1800, tráfico=3, clima=0) → Sin retraso (probabilidad 0.50): el modelo duda, indicando que el patrón no es determinista.

## Conclusión

El modelo de árbol de decisión cumple con el objetivo de aprendizaje supervisado: es entrenado con datos etiquetados, predice correctamente casos nuevos (en este entorno controlado) y permite interpretar las reglas de decisión visualizando el árbol. Para futuras iteraciones se recomienda aumentar el tamaño del dataset y usar datos reales para evaluar la generalización.