Calculadora en Python 🧮

Este proyecto es una calculadora en Python implementada como una clase, con soporte para operaciones básicas y pruebas automatizadas con pytest.

🚀 Instalación y configuración

1️⃣ Instalar Python

Asegúrate de tener Python 3.10 o superior instalado. Puedes descargarlo desde python.org.

Para verificar la instalación:

python --version

2️⃣ Clonar el repositorio

git clone https://github.com/usuario/calculadora-python.git
cd calculadora-python

3️⃣ Crear un entorno virtual (opcional pero recomendado)

python -m venv venv

Activa el entorno virtual:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

4️⃣ Instalar dependencias

pip install -r requirements.txt

Si requirements.txt no existe, instala pytest manualmente:

pip install pytest

🧪 Ejecutar los tests

Para ejecutar las pruebas con pytest, usa:

pytest

Si hay problemas de reconocimiento, prueba con:

python -m pytest

📂 Estructura del proyecto

calculadora-python/
│── mi_proyecto/
│   ├── __init__.py
│   ├── calculadora.py
│── tests/
│   ├── __init__.py
│   ├── test_calculadora.py
│── README.md

✨ Uso de la calculadora

Para ejecutar la calculadora desde la terminal:

python -m mi_proyecto.calculadora
