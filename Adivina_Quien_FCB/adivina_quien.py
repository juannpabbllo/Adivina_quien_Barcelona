import customtkinter as ctk
import json
import os
import random

ARCHIVO_KB = 'base_fcb.json'

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def cargar_base():
    if os.path.exists(ARCHIVO_KB):
        with open(ARCHIVO_KB, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    base = {
        "Lionel Messi": {"nacionalidad": "argentina", "posicion": "delantero", "epoca": "2000-2020", "zurdo": "si", "capitan": "si"},
        "Xavi Hernandez": {"nacionalidad": "españa", "posicion": "mediocampista", "epoca": "2000-2010", "zurdo": "no", "capitan": "si"},
        "Andres Iniesta": {"nacionalidad": "españa", "posicion": "mediocampista", "epoca": "2000-2010", "zurdo": "no", "capitan": "si"},
        "Ronaldinho": {"nacionalidad": "brasil", "posicion": "delantero", "epoca": "2000-2010", "zurdo": "no", "capitan": "no"},
        "Gerard Pique": {"nacionalidad": "españa", "posicion": "defensa", "epoca": "2000-2020", "zurdo": "no", "capitan": "si"},
        "Carles Puyol": {"nacionalidad": "españa", "posicion": "defensa", "epoca": "2000-2010", "zurdo": "no", "capitan": "si"},
        "Pedri": {"nacionalidad": "españa", "posicion": "mediocampista", "epoca": "actual", "zurdo": "no", "capitan": "no"},
        "Gavi": {"nacionalidad": "españa", "posicion": "mediocampista", "epoca": "actual", "zurdo": "no", "capitan": "no"},
        "Lamine Yamal": {"nacionalidad": "españa", "posicion": "delantero", "epoca": "actual", "zurdo": "si", "capitan": "no"}
    }
    with open(ARCHIVO_KB, 'w', encoding='utf-8') as f:
        json.dump(base, f, indent=4, ensure_ascii=False)
    return base

class AkinatorFCB(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Akinator Blaugrana")
        self.geometry("800x700")
        
        self.base_jugadores = cargar_base()
        self.candidatos = list(self.base_jugadores.keys())
        self.preguntas_hechas = set()
        self.atributo_actual = None
        self.valor_actual = None

        self.crear_interfaz()
        self.generar_pregunta()

    def crear_interfaz(self):
        self.frame_top = ctk.CTkFrame(self, fg_color="#1E1E1E", corner_radius=15)
        self.frame_top.pack(pady=20, padx=20, fill="x")

        self.lbl_master = ctk.CTkLabel(self.frame_top, text="🤖 Piensa en un jugador del Barça...", font=("Roboto", 24, "bold"), text_color="#A50044")
        self.lbl_master.pack(pady=10)

        self.lbl_pregunta = ctk.CTkLabel(self.frame_top, text="Cargando sistema...", font=("Roboto", 20))
        self.lbl_pregunta.pack(pady=20)

        self.frame_controles = ctk.CTkFrame(self.frame_top, fg_color="transparent")
        self.frame_controles.pack(pady=10)

        self.crear_botones_juego()

        self.lbl_estado = ctk.CTkLabel(self, text=f"Candidatos posibles: {len(self.candidatos)}", font=("Roboto", 14))
        self.lbl_estado.pack(pady=5)

        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Red Neuronal (Jugadores Activos)")
        self.scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.actualizar_tarjetas()

    def crear_botones_juego(self):
        for widget in self.frame_controles.winfo_children():
            widget.destroy()
            
        btn_si = ctk.CTkButton(self.frame_controles, text="Sí", fg_color="#004D98", hover_color="#003366", command=lambda: self.responder("si"))
        btn_si.grid(row=0, column=0, padx=10)

        btn_no = ctk.CTkButton(self.frame_controles, text="No", fg_color="#A50044", hover_color="#7A0033", command=lambda: self.responder("no"))
        btn_no.grid(row=0, column=1, padx=10)

        btn_nose = ctk.CTkButton(self.frame_controles, text="No lo sé", fg_color="#555555", hover_color="#333333", command=lambda: self.responder("nose"))
        btn_nose.grid(row=0, column=2, padx=10)

    def mostrar_boton_reinicio(self):
        for widget in self.frame_controles.winfo_children():
            widget.destroy()
            
        btn_reiniciar = ctk.CTkButton(self.frame_controles, text="🔄 Jugar de nuevo", fg_color="#DBE721", text_color="black", hover_color="#B8C41A", command=self.reiniciar_juego)
        btn_reiniciar.grid(row=0, column=0, padx=10)

    def reiniciar_juego(self):
        self.candidatos = list(self.base_jugadores.keys())
        self.preguntas_hechas = set()
        
        self.crear_botones_juego()
        self.lbl_master.configure(text="🤖 Piensa en un jugador del Barça...", text_color="#A50044")
        self.actualizar_tarjetas()
        self.generar_pregunta()

    def actualizar_tarjetas(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
            
        for jugador in sorted(self.candidatos):
            card = ctk.CTkFrame(self.scroll_frame, fg_color="#2B2B2B", corner_radius=10)
            card.pack(pady=5, padx=10, fill="x")
            
            lbl_nombre = ctk.CTkLabel(card, text=jugador, font=("Roboto", 16, "bold"))
            lbl_nombre.pack(side="left", padx=15, pady=10)
            
            attrs = self.base_jugadores[jugador]
            tags = f"{attrs.get('posicion', 'Desconocido')} | {attrs.get('nacionalidad', 'Desconocida')} | Época: {attrs.get('epoca', 'Desconocida')}"
            lbl_tags = ctk.CTkLabel(card, text=tags.title(), font=("Roboto", 12), text_color="gray")
            lbl_tags.pack(side="right", padx=15, pady=10)

        self.lbl_estado.configure(text=f"Candidatos posibles: {len(self.candidatos)}")

    def formatear_pregunta(self, atributo, valor):
        atributo = atributo.lower()
        valor = valor.lower()
        
        if atributo == "nacionalidad":
            return f"¿El jugador es de {valor.title()}?"
        elif atributo == "posicion":
            return f"¿El jugador juega como {valor}?"
        elif atributo == "epoca":
            if valor == "actual":
                return "¿Es un jugador de la plantilla actual?"
            else:
                return f"¿El jugador jugó en la época {valor}?"
        elif atributo == "zurdo":
            if valor == "si":
                return "¿El jugador es zurdo?"
            else:
                return "¿El jugador es diestro (patea con la derecha)?"
        elif atributo == "capitan":
            if valor == "si":
                return "¿El jugador ha sido capitán del equipo?"
            else:
                return "¿Es un jugador que NUNCA ha sido capitán?"
        else:
            return f"¿El jugador tiene la característica '{atributo}' como '{valor}'?"

    def generar_pregunta(self):
        if len(self.candidatos) == 1:
            self.adivinar_jugador(self.candidatos[0])
            return
        elif len(self.candidatos) == 0:
            self.rendirse()
            return

        posibles_preguntas = []
        for j in self.candidatos:
            for attr, val in self.base_jugadores[j].items():
                tupla = (attr, val)
                if tupla not in self.preguntas_hechas:
                    posibles_preguntas.append(tupla)

        if not posibles_preguntas:
            # Si se acaban las preguntas pero quedan varios (como Xavi e Iniesta),
            # adivinamos el primero. Si falla, el nuevo código intentará con el siguiente.
            self.adivinar_jugador(self.candidatos[0])
            return

        self.atributo_actual, self.valor_actual = random.choice(posibles_preguntas)
        self.preguntas_hechas.add((self.atributo_actual, self.valor_actual))
        
        pregunta_texto = self.formatear_pregunta(self.atributo_actual, self.valor_actual)
        self.lbl_pregunta.configure(text=pregunta_texto, text_color="white")

    def responder(self, respuesta):
        nuevos_candidatos = []
        
        for j in self.candidatos:
            valor_real = self.base_jugadores[j].get(self.atributo_actual, "").lower()
            
            if respuesta == "si":
                if valor_real == self.valor_actual.lower():
                    nuevos_candidatos.append(j)
            elif respuesta == "no":
                if valor_real != self.valor_actual.lower():
                    nuevos_candidatos.append(j)
            elif respuesta == "nose":
                nuevos_candidatos = self.candidatos
                break
                
        self.candidatos = nuevos_candidatos
        self.actualizar_tarjetas()
        self.generar_pregunta()

    def adivinar_jugador(self, adivinanza):
        self.lbl_pregunta.configure(text=f"¡Lo sé! ¿Estás pensando en {adivinanza}?")
        
        for widget in self.frame_controles.winfo_children():
            widget.destroy()

        btn_correcto = ctk.CTkButton(self.frame_controles, text="¡Sí, es él!", fg_color="green", hover_color="#006400", command=lambda: self.victoria(adivinanza))
        btn_correcto.grid(row=0, column=0, padx=10)

        # Si falla, llama a la nueva función
        btn_falso = ctk.CTkButton(self.frame_controles, text="No, fallaste", fg_color="red", hover_color="#8B0000", command=lambda: self.fallo_adivinanza(adivinanza))
        btn_falso.grid(row=0, column=1, padx=10)

    def fallo_adivinanza(self, adivinanza_erronea):
        # Eliminamos de la lista al jugador que adivinó mal
        if adivinanza_erronea in self.candidatos:
            self.candidatos.remove(adivinanza_erronea)
            
        self.actualizar_tarjetas()
        self.generar_pregunta()

    def victoria(self, jugador):
        self.lbl_pregunta.configure(text=f"¡Soy un genio! Adiviné a {jugador}.", text_color="green")
        self.mostrar_boton_reinicio()

    def rendirse(self):
        self.lbl_pregunta.configure(text="Me rindo... necesito aprender.", text_color="red")
        for widget in self.frame_controles.winfo_children():
            widget.destroy()
            
        self.after(300, self.proceso_aprendizaje)

    def proceso_aprendizaje(self):
        dialog_nombre = ctk.CTkInputDialog(text="¿En qué jugador estabas pensando?", title="Aprender")
        nuevo_jugador = dialog_nombre.get_input()
        
        if nuevo_jugador:
            nacionalidad = ctk.CTkInputDialog(text=f"¿Cuál es la nacionalidad de {nuevo_jugador}?", title="Paso 1/4").get_input()
            posicion = ctk.CTkInputDialog(text=f"¿Cuál es la posición de {nuevo_jugador}? (Ej. delantero, defensa)", title="Paso 2/4").get_input()
            epoca = ctk.CTkInputDialog(text=f"¿De qué época es? (Ej. 2010-2020, actual)", title="Paso 3/4").get_input()
            zurdo = ctk.CTkInputDialog(text=f"¿Es zurdo? (si/no)", title="Paso 4/4").get_input()

            self.base_jugadores[nuevo_jugador.title()] = {
                "nacionalidad": nacionalidad.lower() if nacionalidad else "desconocida",
                "posicion": posicion.lower() if posicion else "desconocida",
                "epoca": epoca.lower() if epoca else "desconocida",
                "zurdo": zurdo.lower() if zurdo else "desconocido"
            }

            with open(ARCHIVO_KB, 'w', encoding='utf-8') as f:
                json.dump(self.base_jugadores, f, indent=4, ensure_ascii=False)
            
            self.lbl_pregunta.configure(text=f"¡Gracias! He creado el perfil completo de {nuevo_jugador.title()}.", text_color="green")
        
        self.mostrar_boton_reinicio()

if __name__ == "__main__":
    app = AkinatorFCB()
    app.mainloop()