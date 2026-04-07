import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import joblib

# ============================================
# 1. CREAR O CARGAR DATASET
# ============================================
try:
    data = pd.read_csv('transporte.csv')
    print("✓ Dataset cargado desde transporte.csv")
except FileNotFoundError:
    print("✓ Creando dataset de ejemplo...")
    data = pd.DataFrame({
        'hora': [800, 815, 830, 845, 900, 915, 930, 945, 1000, 1015, 1100, 1200],
        'trafico': [1, 2, 3, 2, 1, 3, 2, 1, 2, 3, 3, 2],
        'clima': [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],   # CORREGIDO: solo 0 y 1
        'retraso': [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0]
    })
    data.to_csv('transporte.csv', index=False)
    print("✓ Dataset guardado como transporte.csv")

print("\n--- Dataset ---")
print(data.head())
print(f"Total registros: {len(data)}")

# ============================================
# 2. PREPARAR DATOS
# ============================================
X = data[['hora', 'trafico', 'clima']]
y = data['retraso']

# ============================================
# 3. DIVIDIR EN ENTRENAMIENTO Y PRUEBA
# ============================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"\n✓ Entrenamiento: {len(X_train)} registros")
print(f"✓ Prueba: {len(X_test)} registros")

# ============================================
# 4. ENTRENAR ÁRBOL DE DECISIÓN
# ============================================
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)
print("✓ Modelo entrenado (árbol de decisión con max_depth=3)")

# ============================================
# 5. EVALUACIÓN DEL MODELO
# ============================================
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "="*40)
print("RESULTADOS DE EVALUACIÓN")
print("="*40)
print(f"Precisión (accuracy) en test: {accuracy:.2f} ({accuracy*100:.1f}%)")

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['Sin retraso', 'Con retraso']))

# Validación cruzada con 5 pliegues
cv_scores = cross_val_score(modelo, X, y, cv=5)
print(f"\nValidación cruzada (5 folds): {cv_scores}")
print(f"Precisión promedio CV: {cv_scores.mean():.2f} (+/- {cv_scores.std():.2f})")

# ============================================
# 6. PREDICCIONES SOBRE NUEVOS CASOS
# ============================================
nuevos_casos = pd.DataFrame([
    [930, 3, 1],   # hora pico, tráfico alto, lluvia
    [800, 1, 0],   # mañana temprano, tráfico bajo, buen clima
    [1800, 3, 0],  # hora pico tarde, tráfico alto, buen clima
], columns=['hora', 'trafico', 'clima'])

predicciones = modelo.predict(nuevos_casos)
probabilidades = modelo.predict_proba(nuevos_casos)

print("\n" + "="*40)
print("PREDICCIONES PARA NUEVOS CASOS")
print("="*40)
for i, row in nuevos_casos.iterrows():
    estado = "CON retraso" if predicciones[i] == 1 else "SIN retraso"
    prob = probabilidades[i][1] if predicciones[i] == 1 else probabilidades[i][0]
    print(f"Hora={row['hora']}, Tráfico={row['trafico']}, Clima={row['clima']} → {estado} (probabilidad: {prob:.2f})")

# ============================================
# 7. VISUALIZACIÓN DEL ÁRBOL (guardar imagen)
# ============================================
plt.figure(figsize=(12, 8))
plot_tree(modelo, 
          feature_names=['hora', 'trafico', 'clima'], 
          class_names=['Sin retraso', 'Con retraso'], 
          filled=True, 
          rounded=True,
          fontsize=10)
plt.title("Árbol de decisión para predicción de retrasos en transporte masivo", fontsize=14)
plt.savefig('arbol_decision.png', dpi=150, bbox_inches='tight')
print("\n✓ Árbol de decisión guardado como 'arbol_decision.png'")

# ============================================
# 8. GUARDAR MODELO ENTRENADO
# ============================================
joblib.dump(modelo, 'modelo_retrasos.pkl')
print("✓ Modelo guardado como 'modelo_retrasos.pkl'")

print("\n" + "="*40)
print("PROCESO COMPLETADO EXITOSAMENTE")
print("="*40)
