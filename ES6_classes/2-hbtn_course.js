export default class HolbertonCourse {
    constructor (name, length, students) {
        if (typeof name !== 'string') {
            throw new TypeError('Name must be a string');
        }
        if (typeof length != 'number') {
            throw new TypeError('Length must be a number');
        }
        if (!Array.isArray(students) || !students.every(student => typeof student === 'string')) {
            throw new TypeError('Students must be an array of strings');
            }

        this._name = name;
        this._length = length;
        this._students = students;
    }

    get name () {
        return this._name;
    }
    
    set name (person) {
        if (typeof person !== 'string') {
            throw new TypeError('Name must be a string');
        }
        this._name = person;
    }
    
    get length () {
        return this._length;
    }
    set length (long) {
        if (typeof long !== 'number') {
            throw new TypeError('Length must be a number');
        }
        this._length = long;
    }

    get students () {
        return this._students;
    }

    set students (newStudents) {
        if (!Array.isArray(newStudents) || !newStudents.every(student => typeof student === 'string')) {
            throw new TypeError('Students must be an array of strings');
        }
        this._students = newStudents;
    }
}
