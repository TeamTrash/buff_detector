# 🧠 Buff Detector para Lost Ark (EN CONSTRUCCION)

Este proyecto es una herramienta de reconocimiento de imágenes que detecta **buffs activos** en pantalla durante partidas de Lost Ark. Diseñado para jugadores que necesitan automatizar alertas cuando aparecen efectos importantes como buffs de soporte o jefes.

## 🚀 Características

- 🎯 Detección en tiempo real de buffs mediante reconocimiento visual.
- 🔊 Alertas por sonido y ventana emergente cuando se detecta un buff relevante.
- 📸 Personalización de imágenes a reconocer.
- 📍 Áreas configurables de detección para minimizar falsos positivos.
- 💤 Sleep automático tras detección para optimizar rendimiento.

## 🛠️ Requisitos

- Python 3.8+
- Sistema operativo: Windows
- Librerías necesarias:
  pyautogui
  opencv-python
  numpy
  pillow
  tk

## 🤔 Como usarlo

📂 Ingresar a la carpeta.

```bash
cd [nombre-de-la-carpeta]
```

🛠️ Crear un ambiente virtual

```bash
python3 -m venv venv
```

📝 Instalar las dependencias

```bash
pip install -r requirements.txt
```

🚀 Ejecutar el script

```bash
python ./main.py:w
```

⚠️ Advertencia
Este software no interactúa con el juego ni modifica archivos del cliente, por lo tanto no infringe normas de uso. Solo realiza reconocimiento visual en pantalla.
