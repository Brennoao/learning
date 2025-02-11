const returnValue = <T>(value: T) => value // using the sign makes the type of that function dynamic OBS: the signal must be filled with any value passed in the function type

const message = returnValue<string>('hello world')
const count = returnValue<number>(6)

function getFirstValueArray<Type>(array: Type[]) { // it is also possible to pass generics in array
    return array[0]
}

const firstValueFromStringArray = getFirstValueArray<string>(['1', '2'])
const firstValueFromNumberArray = getFirstValueArray<number>([10, 20])

// PROMISES
const returnPromise = async (): Promise<number> => {
    return 5
}