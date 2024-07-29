class HolbertonCourse {
  constructor(name, length, students) {
    this._name = HolbertonCourse._verifyString(name, 'Name');
    this._length = HolbertonCourse._verifyNumber(length, 'Length');
    this._students = HolbertonCourse._verifyArray(students, 'Students');
  }

  static _verifyString(value, attribute) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }

  static _verifyNumber(value, attribute) {
    if (typeof value !== 'number') {
      throw new TypeError(`${attribute} must be a number`);
    }
    return value;
  }

  static _verifyArray(value, attribute) {
    if (!Array.isArray(value) || !value.every((item) => typeof item === 'string')) {
      throw new TypeError(`${attribute} must be an array of strings`);
    }
    return value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = HolbertonCourse._verifyString(value, 'Name');
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this._length = HolbertonCourse._verifyNumber(value, 'Length');
  }

  get students() {
    return this._students;
  }

  set students(value) {
    this._students = HolbertonCourse._verifyArray(value, 'Students');
  }
}

export default HolbertonCourse;
