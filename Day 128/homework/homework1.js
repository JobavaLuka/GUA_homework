let age = prompt("შეიყვანე შენი ასაკი: ")
let ticketPrice = prompt("შეიყვანე ბილეთის საწყისი ფასი: ")

let price

if (age < 0 || ticketPrice < 0) {
    console.log("შეცდომა: მონაცემები უარყოფითია")
} else if (age < 7) {
    price = 0
} else if (age <= 17) {
    price = ticketPrice * 0.5
} else if (age <= 59) {
    price = ticketPrice
} else if (age >= 60) {
    price = ticketPrice * 0.7
}

if (age < 18 || age >= 60) {
    console.log("You have a discount")
}

console.log(`ბილეთის საბოლოო ფასი არის ${price}`)