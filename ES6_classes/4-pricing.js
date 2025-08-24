import Currency from './3-currency';

export default class Pricing {
    constructor (amount, currency) {
        if (typeof amount !== 'number') {
            throw new TypeError("Amount must be a number.")
        }
        if (!(currency instanceof Currency)) {
            throw new TypeError("Currency must be a currency.")
        }
        this._amount = amount;
        this._currency = currency;
    }

    get amount () {
        return this._amount;
    }
    set amount (size) {
        if (typeof size !== 'number') {
            throw new TypeError("Amount must be a number.")
        }
        this._amount = size;
    }
    get currency () {
        return this._currency;
    }
    set currency (coin) {
        if (!(coin instanceof Currency)) {
            throw new TypeError("Currency must be a currency.")
        }
        this._currency = coin;
    }

    displayFullPrice () {
        return `${this.amount} ${this.currency.name} (${this.currency.code})`
    }
    static convertPrice(amount, conversionRate) {
        if (typeof amount !== 'number') {
            throw new TypeError("Amount must be a number");
        }
        if (typeof conversionRate !== 'number') {
            throw new TypeError("Conversion rate must be a number");
        }
        return amount * conversionRate;
    }

}