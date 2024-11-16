from flask import Flask, request, jsonify

app = Flask(__name__)


tareas = []


@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify({'tareas': tareas})


@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    nueva_tarea = {'done': 'true', 'label': request.json['label']}
    tareas.append(nueva_tarea)
    return jsonify({'mensaje': 'Tarea agregada exitosamente'})


@app.route('/tareas/<int:posicion>', methods=['DELETE'])
def eliminar_tarea(posicion):
    try:
       
        if posicion < 1 or posicion > len(tareas):
            return jsonify({'mensaje': 'Posición inválida'}), 400

      
        tarea_eliminada = tareas.pop(posicion - 1)
        return jsonify({'mensaje': f'Tarea eliminada: {tarea_eliminada}'})
    except IndexError:
        return jsonify({'mensaje': 'Posición inválida'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)