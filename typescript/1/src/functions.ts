// IN FUNCTIONS IT IS ALSO POSSIBLE TO USE INTERSECTIONS

const sum = (x: number, y: number): string | number => {
    return (x + y).toString()
}

// VOID = NO RETURN
const log = (message: string): void => {
    console.log(message);
}

interface MathFunc {
    (x: number, y: number) : number
}

const sum1: MathFunc = (x: number, y: number): number => {
    return x + y
}