import json
import os
import urllib.request
from urllib.error import (
    HTTPError,
    URLError,
)

import secret_santa_logic.bring_users as bu
import secret_santa_logic.logic_asignment as la

# from dotenv import load_dotenv

# load_dotenv()


def send_email(asignacion: dict[str, str], personas: dict[str, str]) -> None:
    # 1. Obtenemos la API Key desde las variables de entorno de Render
    api_key = os.getenv("SENDGRID_API_KEY")
    if not api_key:
        print("❌ ERROR: No se encontró la variable SENDGRID_API_KEY en el entorno.")
        return

    # 2. El remitente DEBE ser el correo único que verificaste en SendGrid
    from_email = "jjared.ro@gmail.com"

    # URL oficial de la API de SendGrid
    url = "https://api.sendgrid.com/v3/mail/send"

    # 3. Iteramos sobre tus participantes exactamente como lo hacías tú
    for persona_a in personas.keys():
        correo_destino = personas[persona_a]
        persona_b = asignacion[persona_a]  # A quién le regala

        # Armamos el Payload de SendGrid para ESTE participante en la iteración
        payload = {
            "personalizations": [
                {
                    "to": [{"email": correo_destino}],
                    "subject": "🎄 ¡Tu Amigo Secreto de Secret Santa! 🎄",
                }
            ],
            "from": {"email": from_email, "name": "Secret Santa Bot"},
            "content": [
                {
                    "type": "text/html",
                    "value": f"""
                    <div style="font-family: sans-serif; max-width: 500px; margin: 0 auto; padding: 20px; border: 1px solid #eee; border-radius: 10px;">
                        <h2 style="color: #d32f2f; text-align: center;">¡Hola {persona_a}! 🎁</h2>
                        <p style="font-size: 16px; line-height: 1.5; color: #333;">
                            El sorteo del Amigo Secreto se ha realizado con éxito. Te ha tocado regalar a:
                        </p>
                        <div style="background-color: #e8f5e9; padding: 15px; border-radius: 6px; text-align: center; margin: 20px 0;">
                            <span style="font-size: 22px; font-weight: bold; color: #2e7d32;">✨ {persona_b} ✨</span>
                        </div>
                        <p style="font-size: 14px; color: #777; text-align: center; margin-top: 30px;">
                            ¡Mucho éxito con el regalo y Feliz Navidad! 🎅🎁
                        </p>
                    </div>
                    """,
                }
            ],
        }

        # Configurar la petición HTTP (reemplaza al smtp.send_message)
        req = urllib.request.Request(url, method="POST")
        req.add_header("Authorization", f"Bearer {api_key}")
        req.add_header("Content-Type", "application/json")

        try:
            data = json.dumps(payload).encode("utf-8")
            with urllib.request.urlopen(req, data=data) as response:
                if response.status == 202:
                    print(
                        f"✅ Correo enviado con éxito a {persona_a} ({correo_destino})"
                    )
        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            print(f"❌ Error de SendGrid para {persona_a} ({e.code}): {error_body}")

        # CAMBIA TU ÚLTIMO BLOQUE POR ESTE:
        except URLError as e:
            print(f"❌ Error de red/conexión enviando a {persona_a}: {e.reason}")


if __name__ == "__main__":
    # Obtener las personas desde el archivo CSV
    p = bu.input_users()
    # Realizar la asignación de personas
    a = la.asignment(p)

    # Enviar los correos electrónicos con las asignaciones
    send_email(a, p)
