const fs = require('fs');

function countStudents(path) {
  try {
    // Leer el archivo CSV de forma síncrona
    const data = fs.readFileSync(path, 'utf8');

    // Dividir el contenido en líneas
    const lines = data.trim().split('\n');

    // Filtrar las líneas vacías y procesar solo las válidas
    const students = lines.slice(1).filter((line) => line.trim() !== '');

    // Contar el número total de estudiantes
    console.log(`Number of students: ${students.length}`);

    // Crear un objeto para almacenar los estudiantes por campo
    const fields = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
    });

    // Mostrar la cantidad de estudiantes por campo
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    // Si el archivo no se puede leer o hay algún otro error
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
