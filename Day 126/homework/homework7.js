const accountOwner = "Ana";
let balance = 1000;

balance += 500;
balance -= 250;
balance *= 2;
balance -= 100;
balance /= 2;

console.log(`${accountOwner}'s current balance: ${balance} GEL`);
console.log("Owner type: " + typeof accountOwner);
console.log("Balance type: " + typeof balance);