import pyautogui
import time
import threading
import tkinter as tk
import os
import traceback

# -------- CONFIGURACIÓN -------- #

supports = {
    "artist": [
        { 
            "name": "Sun Well", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 4
        },
        { 
            "name": "Sunsketch", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 8
        },
        { 
            "name": "Drawing Orchids", 
            "image":"assets/artist/drawing_orchids.png" ,
            "uptime": 12
        },
        { 
            "name": "Mir Engrave", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 24
        }
    ],
    "bard": [
        { 
            "name": "Sun Well", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 4
        },
        { 
            "name": "Sunsketch", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 8
        },
        { 
            "name": "Drawing Orchids", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 12
        },
        { 
            "name": "Mir Engrave", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 24
        },
    ],
    "pally": [
        { 
            "name": "Sun Well", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 4
        },
        { 
            "name": "Sunsketch", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 8
        },
        { 
            "name": "Drawing Orchids", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 12
        },
        { 
            "name": "Mir Engrave", 
            "image":"assets/common/placeholder.png" ,
            "uptime": 24
        },
    ]
}

# Región ampliada donde buscar
region_boss_dinamica = (600, 50, 800, 200)

umbral_confianza = 0.60
popup_duration = 2000

# -------- FUNCIONES -------- #

def mostrar_popup(mensaje="✅ BUFF BOSS ACTIVADO"):
    root = tk.Tk()
    root.title("ALERTA")
    root.geometry("320x50+1550+0")
    root.attributes('-topmost', True)
    label = tk.Label(root, text=mensaje, font=("Arial", 18), fg="white", bg="green")
    label.pack(expand=True, fill='both')
    root.after(popup_duration, root.destroy)
    root.mainloop()

# -------- LOOP PRINCIPAL -------- #

def main():
    buff_visible = False
    print("🟢 Monitoreando múltiples buffs... (Ctrl+C para salir)")
    time.sleep(2)

    while True:
        try:
            encontrado = None
            for sup in supports:
                for buff in supports[sup]:
                    imagen = buff['image']
                    try:
                        match = pyautogui.locateOnScreen(
                            imagen,
                            region=region_boss_dinamica,
                            confidence=umbral_confianza
                        )
                        if match:
                            encontrado = match
                            print(f"✅ Detected {imagen} at {match}")
                            break  # Detiene la búsqueda al encontrar el primero
                    except Exception as e:
                        print(f"[ERROR] al buscar {imagen}: {e}")

            actualmente_visible = encontrado is not None

            if actualmente_visible and not buff_visible:
                threading.Thread(target=mostrar_popup, args=("✅ BUFF BOSS ACTIVADO",)).start()
                time.sleep(1)

            buff_visible = actualmente_visible
            time.sleep(1)

        except KeyboardInterrupt:
            print("\n[!] Script detenido por el usuario.")
            break
        except Exception as e:
            print("[ERROR] En el loop principal:")
            traceback.print_exc()
            time.sleep(2)

if __name__ == '__main__':
    main()
