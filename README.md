# Árboles Binarios con Listas en Python

Este proyecto forma parte del trabajo integrador para la asignatura **Programación I** de la **Tecnicatura Universitaria en Programación - UTN**.  
El objetivo es implementar y recorrer **árboles binarios** utilizando listas en Python, con carga de nodos de forma interactiva desde consola.

---

## 👨‍💻 Desarrollado por
- Lautaro Lucero y Gabriela Machin

---

## 🧠 Descripción Técnica

El programa permite construir un **árbol binario** representado mediante listas anidadas, donde cada nodo es una lista con tres elementos: `[valor, hijo_izquierdo, hijo_derecho]`.

El árbol se construye de forma **recursiva e interactiva**, solicitando al usuario el valor de cada nodo y preguntando si desea agregar hijos izquierdo y derecho.

Una vez construido, el árbol se puede recorrer e imprimir utilizando tres métodos clásicos:

- **Preorden** (raíz → izquierda → derecha)
- **Inorden** (izquierda → raíz → derecha)
- **Postorden** (izquierda → derecha → raíz)

Además, se incluye una función que imprime la **estructura del árbol de manera jerárquica**, utilizando indentación para visualizar las relaciones entre los nodos.

---

## 📌 Funcionalidades

- Creación de nodos binarios mediante listas.
- Construcción interactiva del árbol con entrada por consola.
- Verificación de si un nodo es hoja.
- Recorridos en preorden, inorden y postorden.
- Impresión estructurada del árbol.

---

## 📹 Video Demostrativo

Compartimos una demostración del funcionamiento del programa en el siguiente enlace:

🔗 **[[Ver video en YouTube], [(https://youtu.be/evTT8XIm1vU))]**  

---

## 💡 Requisitos

- Python 3.x
- Acceso a consola para ejecutar el script

---

## 🏁 Ejecución

Ejecutar el programa desde la terminal o un entorno de desarrollo compatible:

```bash
python creacion_de_arbol.py
