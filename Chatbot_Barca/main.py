import json
import os
import difflib  


def cargar_base_datos():
    if os.path.exists("base_datos.json"):
        with open("base_datos.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    return {
        "hola": "¡Hola! Bienvenido al Camp Nou digital. ¿En qué puedo ayudarte?",
        "como estas": "¡Excelente! Siempre listo para ver ganar al Barça.",
        "de que te gustaria hablar": "Podemos hablar de Messi, de los títulos o de la alineación actual."
    }


def guardar_base_datos(datos):
    with open("base_datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def chat_barca():
    conocimiento = cargar_base_datos()
    print("---  CHAT CULÉ INTELIGENTE (Aprendizaje Activo)  ---")
    print("(Escribe 'salir' para terminar)")

    while True:

        usuario = input("\nTú: ").lower().strip()

        if usuario == "salir":
            print("Chatbot: ¡Visca el Barça! Hasta pronto.")
            break

        
        preguntas_existentes = list(conocimiento.keys())
        
        coincidencias = difflib.get_close_matches(usuario, preguntas_existentes, n=1, cutoff=0.8)

        if coincidencias:

            mejor_coincidencia = coincidencias[0]
            print(f"Chatbot: {conocimiento[mejor_coincidencia]}")
        else:
            print("Chatbot: Lo siento, no tengo esa información en mi base de datos...")
            nueva_respuesta = input(f"¿Qué debería responder si alguien pregunta '{usuario}'? (o escribe 'saltar'): ")

            if nueva_respuesta.lower() != "saltar":
                conocimiento[usuario] = nueva_respuesta
                guardar_base_datos(conocimiento)
                print("Chatbot: ¡Entendido! He aprendido algo nuevo sobre el club.")
            else:
                print("Chatbot: De acuerdo, continuemos.")

if __name__ == "__main__":
    chat_barca()