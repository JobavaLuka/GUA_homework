const movie = "Avatar";
let ticketPrice = 25;
let tickets = 4;
let snacks = 30;

let totalCost = ticketPrice * tickets;
totalCost += snacks;
totalCost -= 10;

tickets++;

console.log(`Movie: ${movie} | Tickets: ${tickets} | Total: ${totalCost} GEL`);