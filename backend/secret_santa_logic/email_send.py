import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

import secret_santa_logic.bring_users as bu
import secret_santa_logic.logic_asignment as la


def send_email(asignacion: dict[str, str], personas: dict[str, str]) -> None:
    load_dotenv()

    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")

    # 1. Abrimos la conexión con Gmail UNA SOLA VEZ fuera del ciclo
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_user, email_pass)

        # 2. Iteramos sobre los participantes para armar y mandar cada correo
        for persona_a in personas.keys():
            msg = EmailMessage()
            msg["Subject"] = "🎄 ¡Tu Amigo Secreto de Secret Santa! 🎄"
            msg["From"] = email_user
            msg["To"] = personas[persona_a]
            msg.set_content(
                f"Hola {persona_a},\n\n"
                f"Te ha tocado regalar a: {asignacion[persona_a]}.\n\n"
                f"¡Mucho éxito con el regalo y Feliz Navidad! 🎅🎁"
            )

            # Enviar usando la conexión ya abierta
            smtp.send_message(msg)


if __name__ == "__main__":
    # Obtener las personas desde el archivo CSV
    p = bu.input_users()
    # Realizar la asignación de personas
    a = la.asignment(p)

    # Enviar los correos electrónicos con las asignaciones
    send_email(a, p)
