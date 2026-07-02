import React, { useState } from 'react';
import { Plus, Trash2, Gift, Send } from 'lucide-react';

function App() {
  // Estado para manejar la lista dinámica de participantes
  const [participantes, setParticipantes] = useState([
    { nombre: '', correo: '' },
    { nombre: '', correo: '' },
    { nombre: '', correo: '' }, // Empezamos con 3 filas por defecto
  ]);

  // Estados para manejar el flujo de la UI
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [exito, setExito] = useState(false);

  // ==========================================
  // CONFIGURACIÓN AUTOMÁTICA LOCAL vs RENDER
  // ==========================================
  // Detecta automáticamente si la app corre en producción o en tu máquina
  const isProduction = process.env.NODE_ENV === 'production' || import.meta.env?.PROD;
  // const isProduction = true; // <-- Cambia a true para producción, false para desarrollo local

  const API_BASE_URL = isProduction
    ? 'https://secret-santa-backend-05ei.onrender.com'  // <-- PEGA AQUÍ TU URL REAL DE RENDER (la de arriba a la izquierda)
    : 'http://localhost:8000';

  // Función para actualizar los campos de texto dinámicamente
  const handleInputChange = (index, event) => {
    const { name, value } = event.target;
    const nuevosParticipantes = [...participantes];
    nuevosParticipantes[index][name] = value;
    setParticipantes(nuevosParticipantes);
  };

  // Función para añadir una nueva fila de participante (Botón +)
  const agregarFila = () => {
    setParticipantes([...participantes, { nombre: '', correo: '' }]);
  };

  // Función para eliminar una fila específica (Botón bote de basura)
  const eliminarFila = (index) => {
    if (participantes.length <= 2) {
      setError('Debes tener al menos 2 participantes para el intercambio.');
      return;
    }
    setError('');
    const nuevosParticipantes = participantes.filter((_, i) => i !== index);
    setParticipantes(nuevosParticipantes);
  };

  // Función que se ejecuta al enviar el formulario
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    // Filtrar por si acaso quedaron filas completamente vacías al final
    const listaValida = participantes.filter(p => p.nombre.trim() !== '' && p.correo.trim() !== '');

    if (listaValida.length < 2) {
      setError('Por favor, llena los datos de al menos 2 participantes.');
      setLoading(false);
      return;
    }

    // Armamos el Payload exactamente como lo espera FastAPI
    const payload = {
      participantes: listaValida
    };

    try {
      // Petición HTTP POST al backend de FastAPI local
      const response = await fetch(`${API_BASE_URL}/api/secret-santa`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        // Si FastAPI arrojó un error (ej: duplicados), lo capturamos aquí
        throw new Error(data.detail || 'Hubo un problema al procesar el sorteo.');
      }

      // Si todo sale bien, cambiamos al estado de éxito
      setExito(true);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Si el sorteo fue exitoso, mostramos la pantalla de confirmación sin revelar las parejas
  if (exito) {
    return (
      <div style={styles.container}>
        <div style={styles.card}>
          <div style={styles.iconContainer}>
            <Gift size={48} color="#2e7d32" />
          </div>
          <h1 style={styles.title}>¡Sorteo Realizado!</h1>
          <p style={styles.successMessage}>
            El algoritmo ha generado las asignaciones secretas con éxito.
            Cada participante recibirá un correo electrónico en unos instantes con el nombre de su amigo secreto. 🎄🎁
          </p>
          <button style={styles.button} onClick={() => { setExito(false); setParticipantes([{ nombre: '', correo: '' }, { nombre: '', correo: '' }]); }}>
            Crear otro sorteo
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>🎄 Secret Santa 🎅</h1>
        <p style={styles.subtitle}>Agrega a los participantes del intercambio</p>

        {error && <div style={styles.errorAlert}>{error}</div>}

        <form onSubmit={handleSubmit}>
          {participantes.map((participante, index) => (
            <div key={index} style={styles.row}>
              <input
                type="text"
                name="nombre"
                placeholder="Nombre"
                value={participante.nombre}
                onChange={(e) => handleInputChange(index, e)}
                style={styles.input}
                required
              />
              <input
                type="email"
                name="correo"
                placeholder="Correo electrónico"
                value={participante.correo}
                onChange={(e) => handleInputChange(index, e)}
                style={styles.input}
                required
              />
              <button
                type="button"
                onClick={() => eliminarFila(index)}
                style={styles.deleteButton}
                title="Eliminar participante"
              >
                <Trash2 size={18} />
              </button>
            </div>
          ))}

          <div style={styles.actionsContainer}>
            <button type="button" onClick={agregarFila} style={styles.addButton}>
              <Plus size={18} style={{ marginRight: 4 }} /> Añadir Participante
            </button>

            <button type="submit" disabled={loading} style={styles.submitButton}>
              {loading ? 'Procesando...' : (
                <>
                  <Send size={18} style={{ marginRight: 6 }} /> Generar Sorteo
                </>
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

// Estilos en línea sencillos para que se vea genial sin configurar librerías extras de CSS
const styles = {
  container: { display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', backgroundColor: '#f4f6f8', fontFamily: 'system-ui, sans-serif', padding: '20px' },
  card: { backgroundColor: '#ffffff', padding: '30px', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)', width: '100%', maxWidth: '600px' },
  title: { textAlign: 'center', color: '#d32f2f', margin: '0 0 10px 0' },
  subtitle: { textAlign: 'center', color: '#555', marginBottom: '25px' },
  row: { display: 'flex', gap: '10px', marginBottom: '12px', alignItems: 'center' },
  input: { flex: 1, padding: '10px', borderRadius: '6px', border: '1px solid #ccc', fontSize: '14px' },
  deleteButton: { backgroundColor: 'transparent', border: 'none', color: '#d32f2f', cursor: 'pointer', padding: '8px' },
  actionsContainer: { display: 'flex', justifyContent: 'space-between', marginTop: '20px' },
  addButton: { display: 'flex', alignItems: 'center', backgroundColor: '#f0f0f0', border: '1px solid #ccc', padding: '10px 15px', borderRadius: '6px', cursor: 'pointer', fontSize: '14px', color: '#333' },
  submitButton: { display: 'flex', alignItems: 'center', backgroundColor: '#2e7d32', color: '#fff', border: 'none', padding: '10px 20px', borderRadius: '6px', cursor: 'pointer', fontSize: '14px', fontWeight: 'bold' },
  errorAlert: { backgroundColor: '#ffebee', color: '#c62828', padding: '12px', borderRadius: '6px', marginBottom: '15px', fontSize: '14px', borderLeft: '5px solid #c62828' },
  successMessage: { textAlign: 'center', color: '#333', lineHeight: '1.6', marginBottom: '20px' },
  iconContainer: { display: 'flex', justifyContent: 'center', marginBottom: '15px' },
  button: { width: '100%', backgroundColor: '#0288d1', color: '#fff', border: 'none', padding: '12px', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }
};

export default App;
