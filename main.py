import venv
import bring_users as bu
import logic_asignment as la

if __name__ == "__main__":
    # Obtener las personas desde el archivo CSV
    personas = bu.input_users()
    # Realizar la asignación de personas
    la.asignment(personas)