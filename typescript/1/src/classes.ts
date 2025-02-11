interface IPerson {
    id: number;
    sayMyName(): string
}

class Person implements IPerson {
    readonly id: number;
    protected name: string; // protected can only be used within its class os subclass
    private age: number

    constructor(id: number, name: string, age: number) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    sayMyName(): string {
        return this.name
    }
} // to use an interface in a class, you need to put the implements parameter

class Employee extends Person {
    constructor(id: number, name: string, age: number) {
        super(id, name, age)
    }

    whoAmi() {
        return this.name
    }
}
