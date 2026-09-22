let age = prompt("შიყვანე შენი ასაკი")
let ticketType = prompt("შიყვანე ბილეთის (standard / vip) ტიპი").toLowerCase()
let name = prompt("შიყვანე შენი სახელი").trim()

let price

if (age <= 0) {
    console.log("არასწორი ასაკი")
} else if (age < 12) {
    price = 5
} else if (age >= 12 && age <= 17) {
    price = 8
} else if (age >= 18) {
    price = 15
}

if (ticketType === "vip") {
    price += 10
} else if (ticketType === "standard") {
    price = price
} else {
    console.log("ბილეთის ტიპი არასწორია")
}

if (name === "admin") {
    console.log("ადმინისტრატორისთვის ბილეთი უფასოა")
}

console.log(`მომხმარებლის სახელი არის ${name} და ბილეთის ფასი არის ${price}`)