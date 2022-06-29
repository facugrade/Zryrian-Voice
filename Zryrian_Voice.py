import pyttsx3
import tkinter as tk
engine = pyttsx3.init()

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("ZryrianVoice")


def sf():
    orden = decir.get()
    engine.say(orden)
    engine.runAndWait()


decir = tk.Entry()
decir.place(x=135, y=120)

boton = tk.Button(text="Click para reproducir!!", command=sf)
boton.place(x=135, y=160)



ventana.mainloop()