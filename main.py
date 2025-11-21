import venv
import bring_users as bu
import logic_asignment as la
import email_send as es

def run_secret_santa():
    # Obtener las personas desde el archivo CSV
    personas = bu.input_users()
    print("Users imported successfully!")
    # Realizar la asignación de personas
    la.asignment(personas)
    print("Assignment completed successfully!")
    # Enviar los correos electrónicos con las asignaciones
    es.send_email(la.asignment(personas), personas)
    print("Emails sent successfully!") 

if __name__ == "__main__":
    run_secret_santa()