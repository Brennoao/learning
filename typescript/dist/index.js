"use strict";
// BASICS TYPES
let age = 5; // number
const firstName = 'Brenno'; // string
const isValid = true; // boolean
let idk = 5; // dynamic types
// IF VARIABLE IS NOT ASSINED A VALUE, ITS TYPE WILL BE INFERRED AS THE TYPE OF THE ASSINED VALUE IF IT A SINGLE VALUE
// ARRAYS TYPES
const ids = [1, 2, 3, 4, 5, 6]; // type number
const boolean = [true, false, true, false]; // type boolean
const names = ['Brenno', 'Lucas', 'João', 'Osvaldo']; // type string
// TYPE TUPLE
const person = [1, 'String']; // tuple type is basically an array but with a predifined order, it cannot be changed later
// TUPLE LIST
const peaple = [
    [1, 'Brenno'],
    [2, 'Lucas'],
]; // tuple list typle is an array of tuples
// INTERSECTION
const productID = true; // declares more than one type
// ENUM
var Direction;
(function (Direction) {
    Direction[Direction["up"] = 1] = "up";
    Direction[Direction["down"] = 2] = "down";
})(Direction || (Direction = {})); // assingn a value to another value
const direction = Direction.up;
// TYPE ASSERTIONS
const productName = 'Boné';
// let itemId: string
//let itemId = productName as string // first type
let itemId = productName; // second type
// change the type of the variable
