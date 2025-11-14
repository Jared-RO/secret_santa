import pandas as pd
import venv

def input_users():
    # Leer el archivo CSV y devolver un diccionario de personas
    df = pd.read_csv('./users_file/users.csv', header=0)
    personas = pd.Series(df.Correo.values, index=df.Nombre_Usuario).to_dict()
    return personas

if __name__ == "__main__":
    print(input_users())  