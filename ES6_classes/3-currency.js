export default class Currency {
    constructor (code, name) {
        if (typeof code !== 'string') {
            throw new TypeError("Code must be a string.")
        }
        if (typeof name !== 'string') {
            throw new TypeError("Name must be a string.")
        }
        this._code = code;
        this._name = name;
    }

    get code () {
        return this._code;
    }

    set code (binary) {
        if (typeof binary !== 'string') {
            throw new TypeError('Code must be a string');
        }    
        this._code = binary;
    }
    
    get name () {
        return this._name
    }

    set name (person) {
        if (typeof person !== 'string') {
            throw new TypeError('Name must be a string');
        }    
        this._name = person;
    }

    displayFullCurrency () {
        return `${this.name} (${this.code})`
    }
}