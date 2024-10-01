import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase('./database.csv');
      const response = ['This is the list of our students'];

      for (const field in students) {
        if (Object.prototype.hasOwnProperty.call(students, field)) {
          response.push(`Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}`);
        }
      }

      res.status(200).send(response.join('\n'));
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor({ params: { major } }, res) {
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase('./database.csv');
      const list = students[major] || [];

      if (list.length === 0) {
        return res.status(200).send(`List: No students found for ${major}`);
      }

      return res.status(200).send(`List: ${list.join(', ')}`); // Retorno aquí también
    } catch (error) {
      return res.status(500).send('Cannot load the database'); // Agregando retorno aquí
    }
  }
}

export default StudentsController;
