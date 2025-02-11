"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const returnValue = (value) => value; // using the sign makes the type of that function dynamic OBS: the signal must be filled with any value passed in the function type
const message = returnValue('hello world');
const count = returnValue(6);
function getFirstValueArray(array) {
    return array[0];
}
const firstValueFromStringArray = getFirstValueArray(['1', '2']);
const firstValueFromNumberArray = getFirstValueArray([10, 20]);
// PROMISES
const returnPromise = () => __awaiter(void 0, void 0, void 0, function* () {
    return 5;
});
