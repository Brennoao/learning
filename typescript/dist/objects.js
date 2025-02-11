"use strict";
const user = {
    firstName: 'Brenno',
    age: 20,
    email: 'test@test.com',
    orders: [{ productId: '1', price: 200 }],
    refister() {
        return 'a';
    }
};
const author = {
    age: 2,
    books: ['1'],
    email: 'author@test.com',
    firstName: 'Sei',
    orders: [{ productId: '1', price: 2 }], // can also be an empty array
    refister() {
        return 'a';
    }
};
const emailUser = {
    email: 'test@test.com',
    firstName: 'test'
};
const newAuthor = {
    email: 'test@test.com',
    firstName: 'Felipe',
    books: []
};
const grade = 1;
// OBS: OPTIONAL PROPERTIES MAY GIVE AN ERROR IF PASSED IN MANDATORY PROPERTIES
