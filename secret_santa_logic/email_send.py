import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

import secret_santa_logic.bring_users as bu
import secret_santa_logic.logic_asignment as la


def send_email(asignacion: dict[str, str], personas: dict[str, str]) -> None:
    load_dotenv()
    for persona_a in personas.keys():
        # Crear el mensaje
        msg = EmailMessage()
        msg["Subject"] = "Secret Santa!!"
        msg["From"] = os.getenv("EMAIL_USER")  # cambiar por correo de la aplicacion
        msg["To"] = personas[persona_a]
        msg.set_content(
            f"Hola {persona_a}\nTe ha tocado regalar a {asignacion[persona_a]}.\n\n¡Feliz Navidad!"
        )

        # Enviar el mensaje usando SMTP de Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(
                os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS")
            )  # cambiar por correo y contraseña de la aplicacion
            smtp.send_message(msg)


if __name__ == "__main__":
    # Obtener las personas desde el archivo CSV
    p = bu.input_users()
    # Realizar la asignación de personas
    a = la.asignment(p)

    # Enviar los correos electrónicos con las asignaciones
    send_email(a, p)
