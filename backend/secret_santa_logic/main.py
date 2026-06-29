from fastapi import (
    BackgroundTasks,
    FastAPI,
    HTTPException,
)
from fastapi.middleware.cors import CORSMiddleware
from secret_santa_logic.email_send import send_email  # Usando tu file real
from secret_santa_logic.logic_asignment import asignment  # Usando tu file real
from secret_santa_logic.schemas import (
    AsignacionResponse,
    SecretSantaRequest,
)

app = FastAPI(title="Secret Santa API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/secret-santa", response_model=AsignacionResponse)
async def procesar_secret_santa(
    request: SecretSantaRequest, background_tasks: BackgroundTasks
) -> dict[str, dict[str, str]]:
    participantes = request.participantes

    if len(participantes) < 2:
        raise HTTPException(
            status_code=400, detail="Deben haber al menos 2 participantes."
        )

    # Validar duplicados
    correos = [p.correo.lower() for p in participantes]
    if len(correos) != len(set(correos)):
        raise HTTPException(
            status_code=400, detail="No se permiten correos duplicados."
        )

    nombres = [p.nombre.strip() for p in participantes]
    if len(nombres) != len(set(nombres)):
        raise HTTPException(
            status_code=400, detail="No se permiten nombres duplicados."
        )

    try:
        # Convertimos el formato de Pydantic al diccionario que espera tu algoritmo anterior
        # formato: {"Nombre": "correo@gmail.com"}
        personas_dict = {p.nombre: p.correo for p in participantes}

        # Ejecutar tu algoritmo
        parejas_asignadas = asignment(personas_dict)

        # Enviar correos usando tu función existente en segundo plano
        background_tasks.add_task(send_email, parejas_asignadas, personas_dict)

        return {"parejas": parejas_asignadas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


# if __name__ == "__main__":
#     run_secret_santa()
