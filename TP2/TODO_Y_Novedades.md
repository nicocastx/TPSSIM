# TODOs y Novedades del Proyecto

## ✅ Novedades (por Ale)

### Cambios en la Distribución Normal
- ✅ Cambiado el método de generación: ahora se utiliza Box-Muller en lugar de `random.gauss`.
- ✅ Validación de campos en la interfaz normal implementada.
- ✅ La generación RND está en `logicaDistribuciones/utilidades.py`.

### Cambios en la Distribución Exponencial
- ✅ Validación básica de campos implementada.
- ✅ Interfaz modificada para permitir selección entre μ o λ, con conversión automática.

---

## 🔧 TODOs Generales

- [ ] Corregir función de copia para que también copie los valores decimales.
- [ ] Permitir reingreso de datos en las tablas de formulario (ocultarlos o reiniciar entradas).

---

## 🔍 TODOs por Sección

### Distribución Normal
- [x] Revisar el uso de la función de distribución: se verificó que `random.gauss` no era lo ideal.
- [x] Aplicado método de Box-Muller.
- [x] Validaciones de campos.

### Distribución Exponencial
- [ ] Verificar si la validación de campos es la correcta.
- [x] Agregada interfaz para selección de μ o λ.