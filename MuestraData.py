from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage,Toplevel,filedialog,messagebox
from fpdf import FPDF
import datetime as dt

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def exportar_pdf(mensajes, participantes, parent_window): #Esto es para los pdf, se estiliza desde el codigo
    archivo = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Archivo PDF", "*.pdf")],
        parent=parent_window  # Evita se genere una ventana vacía
    )
    if not archivo:
        return
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14,style="B")
    pdf.cell(200, 10, txt="Resumen de Chat - Empresa XXXXX", ln=True, align="C")
    pdf.ln(4)
    pdf.set_font("Arial", size=8,style="I")
    fecha = dt.date.today()
    pdf.cell(200, 10, txt=f"Fecha de reporte: {fecha}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=12,style="B")
    pdf.cell(200, 10, txt="Informacion general del chat:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Total de mensajes: {mensajes}", ln=True)
    pdf.cell(200, 10, txt=f"Total de participantes: {len(participantes)}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=12,style="B")
    pdf.cell(200, 10, txt="Detalles de los participantes:", ln=True)
    pdf.set_font("Arial", size=12)
    def safe_latin1(txt: str) -> str:
        return txt.encode("latin-1", "replace").decode("latin-1")
    for nombre, cantidad in participantes.items():
        lineas_mensajes = f"{nombre} ha enviado {cantidad} mensajes."
        pdf.cell(200, 10, txt=safe_latin1(lineas_mensajes), ln=True)
    pdf.output(archivo)
    messagebox.showinfo("¡Listo!", "PDF guardado correctamente.", parent=parent_window)


def mostrar_resumen(total_mensajes, participantes_dict, parent): #Funcion que muestra la parte grafica
    window = Toplevel(parent) #Se toma la window como parent
    window.title("SmsCounter")
    window.geometry("500x400")
    window.configure(bg="#000000")
    icon_png = relative_to_assets("mi_icono.png")      
    img = PhotoImage(file=icon_png)                    
    window.iconphoto(False, img)                      
    window._icon = img                                 

    canvas = Canvas(
        window,
        bg="#000000",
        height=400,
        width=500,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Carga de imágenes con referencias persistentes
    window.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(250.0, 200.0, image=window.image_1)

    window.image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(250.0, 271.0, image=window.image_2)

    window.image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(250.0, 136.0, image=window.image_3)

    window.image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    canvas.create_image(250.0, 92.0, image=window.image_4)

    window.image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    canvas.create_image(85.0, 173.0, image=window.image_5)

    window.image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    canvas.create_image(112.0, 139.0, image=window.image_6)

    window.image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    canvas.create_image(139.0, 96.0, image=window.image_7)

    window.image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
    canvas.create_image(250.0, 36.0, image=window.image_8)

    # Mostrar total de mensajes y número de participantes
    canvas.create_text(
        430,
        79.0,
        anchor="nw",
        text=str(total_mensajes), #mensajes totales
        fill="#FFFFFF",
        font=("Inter SemiBold", 24 * -1)
    )
    canvas.create_text(
        430,
        122.0,
        anchor="nw",
        text=str(len(participantes_dict)), #total de participantes, basicamente muestra la longitud de la lista
        fill="#FFFFFF",
        font=("Inter SemiBold", 24 * -1)
    )

    # Mostrar mensajes por participante
    name_limit = 0
    y = 200
    for nombre, cantidad in sorted(participantes_dict.items(), key=lambda x: x[1], reverse=True):
        if name_limit >= 8:
            canvas.create_text(
            250,
            y,
            anchor="center",
            text=f"Para ver mas detalles de los participantes debes generar el .PDF", #Se toma de los items obtenido, solo es un separacion
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
            )
            break
        canvas.create_text(
            250,
            y,
            anchor="center",
            text=f"{nombre} ha enviado {cantidad} mensajes.", #Se toma de los items obtenido, solo es un separacion
            fill="#FFFFFF",
            font=("Inter", 14 * -1)
        )
        y += 20
        name_limit += 1

    # Botón
    btn_img = PhotoImage(file=relative_to_assets("button_1.png"))
    setattr(window, "btn_img", btn_img)  # referencia persistente
    btn = Button(window,
                    image=btn_img,
                    borderwidth=0,
                    relief="flat",
                    bg="#70230e",
                    command=lambda: exportar_pdf(total_mensajes, participantes_dict, window))
    #llamar boton al canvas
    canvas.create_window(250, 370, window=btn, width=181, height=28)
    
    def on_close(): #Para eliminar la ventana y cerrar el proceso
        parent.destroy()
        
    window.protocol("WM_DELETE_WINDOW", on_close) #Detecta si se da a la x en la ventana
    window.resizable(False, False)
