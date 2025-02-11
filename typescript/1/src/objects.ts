// TYPE / ALSO THE POSSIBILITY OF USING TYPES TOGETHER
type Order = {
    productId: string,
    price: number
}

type User = {
    firstName: string,
    age: number,
    email: string,
    password?: string, // the question mark removes the mandatory nature of the property, making it optional
    orders: Order[],
    refister(): string // IN FUNCTIONS TO MAKE THE OPTIONAL THE QUESTION MARK GOES BEFORE THE PARENTHESES
}
const user: User = {
    firstName: 'Brenno',
    age: 20,
    email: 'test@test.com',
    orders: [{ productId: '1', price: 200 }],
    refister() {        
        return 'a'
    }
}

//UNIONS
type Author = {
    books: string[]
}

const author: Author & User = {
    age: 2,
    books: ['1'],
    email: 'author@test.com',
    firstName: 'Sei',
    orders: [{ productId: '1', price: 2 }], // can also be an empty array
    refister() {        
        return 'a'
    }
}

// INTERFACE

interface UserInterface {
    readonly firstName: string, // READYONLY PROPERTY MAKES THAT PROPERTY READ-ONLY 
    email: string
}

const emailUser: UserInterface = {
    email: 'test@test.com',
    firstName: 'test'
} 

interface AuthorInterface {
    books: string[]
}

const newAuthor: UserInterface & AuthorInterface = {
    email: 'test@test.com',
    firstName: 'Felipe',
    books: []
}

type Grade = number | string // this mode cannot be used interfaces
const grade: Grade = 1

// OBS: OPTIONAL PROPERTIES MAY GIVE AN ERROR IF PASSED IN MANDATORY PROPERTIES