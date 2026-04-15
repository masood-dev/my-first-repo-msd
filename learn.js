// ===== JavaScript Basics =====

// 1. Variables
let name = "Alice";
const age = 25;
var city = "New York"; // older way, prefer let/const

// 2. Data Types
let str = "Hello, World!";
let num = 42;
let float = 3.14;
let bool = true;
let nothing = null;
let undef = undefined;

// 3. String Operations
console.log("Name:", name);
console.log("Greeting:", str.toUpperCase());
console.log(`Template literal: My name is ${name} and I am ${age} years old.`);

// 4. Arrays
let fruits = ["apple", "banana", "cherry"];
fruits.push("mango");
console.log("Fruits:", fruits);
console.log("First fruit:", fruits[0]);
console.log("Length:", fruits.length);

// 5. Objects
let person = {
    name: "Bob",
    age: 30,
    city: "London",
    greet: function () {
        return `Hi, I'm ${this.name}!`;
    }
};
console.log(person.greet());
console.log("City:", person.city);

// 6. Conditionals
if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// Ternary
let status = age >= 18 ? "Adult" : "Minor";
console.log("Status:", status);

// 7. Loops
for (let i = 0; i < 5; i++) {
    process.stdout.write(i + " ");
}
console.log();

// For...of loop
for (let fruit of fruits) {
    console.log("Fruit:", fruit);
}

// 8. Functions
function add(a, b) {
    return a + b;
}

// Arrow function
const multiply = (a, b) => a * b;

console.log("Sum:", add(3, 7));
console.log("Product:", multiply(4, 5));

// 9. Array Methods
let numbers = [1, 2, 3, 4, 5];
let doubled = numbers.map(n => n * 2);
let evens = numbers.filter(n => n % 2 === 0);
let total = numbers.reduce((acc, n) => acc + n, 0);

console.log("Doubled:", doubled);
console.log("Evens:", evens);
console.log("Total:", total);

// 10. Destructuring
let [first, second, ...rest] = fruits;
let { name: personName, age: personAge } = person;

console.log("First:", first, "| Second:", second, "| Rest:", rest);
console.log("Person:", personName, personAge);
