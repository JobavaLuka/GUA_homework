let health = 100;
let level = 1;
let coins = 50;
const player = "Warrior";

health -= 25;
coins += 40;
level ++;
coins *= 2;
health /= 5;

console.log(`${player} | Level: ${level} | Health: ${health} | Coins: ${coins}`);