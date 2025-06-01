// 10-car.js
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // create new instance of the exact class of this object (supporting inheritance)
    const Cls = this.constructor;
    return new Cls();
  }
}
