"use strict";
class Person {
    constructor(id, name, age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }
    sayMyName() {
        return this.name;
    }
} // to use an interface in a class, you need to put the implements parameter
class Employee extends Person {
    constructor(id, name, age) {
        super(id, name, age);
    }
    whoAmi() {
        return this.name;
    }
}
