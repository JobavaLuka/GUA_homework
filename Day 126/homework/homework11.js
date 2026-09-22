const username = "Saba";
let age = 16;
let balance = 250;
let purchases = 2;
const currency = "GEL";
const shopName = "Digital Shop";

purchases += 3;
balance -= 3 * 40;
balance += 150;
balance -= 25;
age ++;
balance *= 2;

console.log(`User: ${username}`);
console.log(`Age: ${age}`);
console.log(`Purchases: ${purchases}`);
console.log(`Balance: ${balance} ${currency}`);
console.log(`Shop: ${shopName}`);

console.log(typeof username);
console.log(typeof age);
console.log(typeof balance);
console.log(typeof purchases);
console.log(typeof currency);
console.log(typeof shopName);