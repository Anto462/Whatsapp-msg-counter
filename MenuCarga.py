from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Logica import ProcesarChat #se llama la logica
import MuestraData

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame1"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def iniciar_analisis(window): #cuando se inicia un analisis
    mensajes, participantes = ProcesarChat(window) #se manda a prccesar el chat
    if mensajes is not None: #si se obtuvo respuesta
        window.withdraw()  #se oculta la ventana que muestra el boton
        MuestraData.mostrar_resumen(mensajes, participantes, window) #se muestra la nueva ventana, se envia la window que sera interpretada como parent

window = Tk() #De aca para abajo es diseño

window.title("SmsCounter")
window.geometry("500x400")
window.configure(bg = "#000000")
icon_png = relative_to_assets("mi_icono.png")      
img = PhotoImage(file=icon_png)                    
window.iconphoto(False, img)                     
window._icon = img                                


canvas = Canvas(
    window,
    bg = "#000000",
    height = 400,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    250.0,
    200.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    254.9999993866434,
    200.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    181.0,
    152.0,
    image=image_image_3
)

canvas.create_text(
    137.0,
    279.0,
    anchor="nw",
    text="Presiona para elegir el .txt a analizar:",
    fill="#FFFFFF",
    font=("RobotoRoman Medium", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg="#70230e",
    command=lambda: iniciar_analisis(window), #Aca llama a la funcion
    relief="flat"
)
button_1.place(
    x=182.0,
    y=301.0,
    width=135.0,
    height=66.0
)
window.resizable(False, False)
window.mainloop()
