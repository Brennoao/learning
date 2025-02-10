// BASICS TYPES
let age: number = 5 // number
const firstName: string = 'Brenno' // string
const isValid: boolean = true // boolean
let idk: any = 5 // dynamic types

// IF VARIABLE IS NOT ASSINED A VALUE, ITS TYPE WILL BE INFERRED AS THE TYPE OF THE ASSINED VALUE IF IT A SINGLE VALUE

// ARRAYS TYPES
const ids: number[] = [1, 2, 3, 4 , 5, 6] // type number
const boolean: boolean[] = [true, false, true, false] // type boolean
const names: string[] = ['Brenno', 'Lucas', 'João', 'Osvaldo'] // type string

// TYPE TUPLE
const person: [number, string] = [1, 'String'] // tuple type is basically an array but with a predifined order, it cannot be changed later

// TUPLE LIST
const peaple: [number, string][] = [
    [1, 'Brenno'],
    [2, 'Lucas'],
] // tuple list typle is an array of tuples

// INTERSECTION
const productID: string | number | boolean = true // declares more than one type

// ENUM
enum Direction {
    up = 1,
    down = 2
} // assingn a value to another value

const direction  = Direction.up

// TYPE ASSERTIONS
const productName: any = 'Boné'
// let itemId: string

//let itemId = productName as string // first type
let itemId = <string>productName     // second type

// change the type of the variable