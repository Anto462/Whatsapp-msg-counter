from tkinter import filedialog, Tk, Toplevel

def ProcesarChat(parent): #Funcion tras presionar boton
    chat = filedialog.askopenfilename(filetypes=[("Archivos TXT", "*.txt")], parent=parent) #Se asocia a la pestaña creada

    if not chat: #Si no hayt chat elegido no pasa nada, luego agregar un mensaje
        return None, None

    with open(chat, "r", encoding="utf-8") as f: #Leer cada linea  de texto dentro del chat en UTF8 en las lines
        lines = f.readlines()

    messages = 0 #contador sms
    contador = {} #Almacen

    for line in lines: #Por cada linea
        if "M]" in line or "M -" in line or "m. -" in line: #Esto es por la estrucutra que exporta los mensajes whatsapp
            end_of_date = line.find("]") if "]" in line else line.find("-") #Mismo, es para encontrar donde termina, en general hasta el siguiente comentario es solo para encontrar el sms
            if end_of_date == -1:
                continue
            z = line.find(": ", end_of_date)
            if z == -1:
                continue
            participant = line[end_of_date+1:z].strip() #Se añade la linea del mensaje
            participant = participant.replace("AM", "").replace("PM", "").replace("M", "").replace("-", "").replace(".", "").strip() #Limpia el nombre del participante
            if "cifrado" in participant.lower() or "mensajes" in participant.lower(): #si dice cifrado o mensajes se ignora, esto es para ignorar los mensajes de sistema
                continue
            contador[participant] = contador.get(participant, 0) + 1 #Se suma el mensaje al participante que lo envio
            messages += 1 #se aumenta la cantidad de mensajes

    return messages, contador
