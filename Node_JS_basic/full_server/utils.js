import fs from 'fs/promises';

const readDatabase = async (filePath) => {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = {};

    lines.slice(1).forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (!students[field]) students[field] = [];
      students[field].push(firstname);
    });

    return students;
  } catch (error) {
    throw new Error('Database not found');
  }
};

export default readDatabase;
