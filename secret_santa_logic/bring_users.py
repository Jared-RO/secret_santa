import pandas as pd


def input_users() -> dict[str, str]:
    """Función para leer el archivo CSV y devolver un diccionario de personas."""
    # Leer el archivo CSV y devolver un diccionario de personas
    df = pd.read_csv("./users_file/users.csv", header=0)
    personas: dict[str, str] = pd.Series(
        df.Correo.values, index=df.Nombre_Usuario
    ).to_dict()
    return personas


if __name__ == "__main__":
    print(input_users())
