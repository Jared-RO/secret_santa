import smtplib
from email.message import EmailMessage
import venv
import bring_users as bu
import logic_asignment as la
from dotenv import load_dotenv
import os


def send_email(asignacion, personas):
    load_dotenv()
    for persona_a in personas.keys():
        # Crear el mensaje
        msg = EmailMessage()
        msg["Subject"] = "Secret Santa!!"
        msg["From"] = os.getenv("EMAIL_USER")  # cambiar por correo de la aplicacion
        msg["To"] = personas[persona_a]
        msg.set_content(
            f"Hola {persona_a}!\nTe ha tocado regalar a {asignacion[persona_a]}. \n\n¡Feliz Navidad!"
        )

        # Enviar el mensaje usando SMTP de Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(
                os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS")
            )  # cambiar por correo y contraseña de la aplicacion
            smtp.send_message(msg)


if __name__ == "__main__":
    # Obtener las personas desde el archivo CSV
    personas = bu.input_users()
    # Realizar la asignación de personas
    asignacion = la.asignment(personas)

    # Enviar los correos electrónicos con las asignaciones
    send_email(asignacion, personas)
