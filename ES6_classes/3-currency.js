class Currency {
  constructor(code, name) {
    this._code = this.verifyStr(code, 'Code');
    this._name = this.verifyStr(name, 'Name');
  }

  verifyStr(value, attribute) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }
  
  get code() {
    return this._code;
  }
  
  set code(value) {
    this._code = this.verifyStr(value, 'Code');
  }
  
  get name() {
    return this._name;
  }
  
  set name(value) {
    this._name = this.verifyStr(value, 'Name');
  }
  
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
  
export default Currency;
