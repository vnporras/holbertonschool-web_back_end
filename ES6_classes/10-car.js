export default class Car {
    constructor(brand, motor, color) {
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    cloneCar() {
      const cloned = new this.constructor();
      cloned._brand = undefined;
      cloned._motor = undefined;
      cloned._color = undefined;
      return cloned;
    }
  }
  