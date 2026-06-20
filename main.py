import secret_santa_logic.bring_users as bu
import secret_santa_logic.email_send as es
import secret_santa_logic.logic_asignment as la


def run_secret_santa() -> dict[str, str]:
    """Función principal para ejecutar el proceso de Secret Santa."""
    # Obtener las personas desde el archivo CSV
    personas = bu.input_users()
    print("Users imported successfully!")
    # Realizar la asignación de personas
    asignacion = la.asignment(personas)
    print("Assignment completed successfully!")
    # Enviar los correos electrónicos con las asignaciones
    es.send_email(asignacion, personas)
    print("Emails sent successfully!")
    return asignacion


if __name__ == "__main__":
    run_secret_santa()
