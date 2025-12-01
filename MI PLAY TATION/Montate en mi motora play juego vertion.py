import tkinter as tk
import random
import webbrowser

VIDEO_URL = "https://www.youtube.com/watch?v=LXqIq4OxSk4"

# ---------------------------
# LISTA DE ACERTIJOS
# ---------------------------

ACERTIJOS = [
    {
        "pregunta": "Víctor le dice a Joel. ¿Qué le dice?",
        "respuesta": "montate en mi motora"
    },
    {
        "pregunta": "Pero Joel le dice a Víctor. ¿Qué le dice?",
        "respuesta": "desayuna con huevo"
    },
    {
        "pregunta": "Pero de momento Víctor le dice a Joel. ¿Qué le dice?",
        "respuesta": "toma mango"
    },
    {
        "pregunta": "De repente entonces Joel le dice a Víctor. ¿Qué le dice?",
        "respuesta": "quisiera ser una mosca para pararme en tu piel"
    },
    {
        "pregunta": "De repente Víctor le dice a Joel. ¿Qué soy?",
        "respuesta": "yo soy yo"
    },
    {
        "pregunta": "De momento Joel le dice a Víctor. ¿Qué le dice?",
        "respuesta": "feliz navidad"
    }
]

# ---------------------------
# FUNCIONES DEL JUEGO
# ---------------------------

def nuevo_acertijo():
    """Elige un acertijo aleatorio."""
    global actual
    actual = random.choice(ACERTIJOS)
    lbl_pregunta.config(text="🧩 Acertijo:\n\n" + actual["pregunta"])
    entrada.delete(0, tk.END)
    resultado.set("")

def verificar():
    """Verifica si la respuesta es correcta."""
    user = entrada.get().lower().strip()

    if not user:
        resultado.set("❗ Escribe una respuesta.")
        return

    if user == actual["respuesta"]:
        resultado.set("✅ ¡Correcto! Cargando otro acertijo...")
        root.after(1500, nuevo_acertijo)
    else:
        resultado.set("❌ Incorrecto. Intenta de nuevo.")

def abrir_video():
    """Abre el video en el navegador."""
    webbrowser.open(VIDEO_URL)

# ---------------------------
# INTERFAZ TKINTER
# ---------------------------

root = tk.Tk()
root.title("Juego de Acertijos 🧠")
root.geometry("500x350")  # aumente un poco la altura para el mensaje extra
root.resizable(False, False)

lbl_titulo = tk.Label(root, text="🎉 JUEGO DE ACERTIJOS 🎉", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# Mensaje para ver el video antes de responder
frame_video = tk.Frame(root)
frame_video.pack(pady=5)

lbl_video = tk.Label(
    frame_video, 
    text="📺 Mira este video antes de responder las preguntas:", 
    font=("Arial", 11), 
    fg="darkred"
)
lbl_video.pack(side=tk.LEFT)

btn_video = tk.Button(frame_video, text="Ver video", font=("Arial", 11), command=abrir_video)
btn_video.pack(side=tk.LEFT, padx=5)

lbl_pregunta = tk.Label(root, text="", wraplength=460, justify="center", font=("Arial", 13))
lbl_pregunta.pack(pady=15)

entrada = tk.Entry(root, font=("Arial", 14), width=26)
entrada.pack()

btn = tk.Button(root, text="Responder", font=("Arial", 12), command=verificar)
btn.pack(pady=10)

resultado = tk.StringVar()
lbl_res = tk.Label(root, textvariable=resultado, font=("Arial", 12), fg="blue")
lbl_res.pack(pady=10)

# Cargar primer acertijo
nuevo_acertijo()

root.mainloop()
