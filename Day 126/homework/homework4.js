let price = 80;
let quantity4 = 4;
let discount = 20;
const currency = "GEL";

let total = price * quantity4;
total -= discount;

console.log("Total: " + total + " " + currency);
console.log(`Total: ${total} ${currency}`);

console.log(typeof price);
console.log(typeof quantity4);
console.log(typeof discount);
console.log(typeof currency);