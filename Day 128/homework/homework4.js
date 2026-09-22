let number = Number(prompt("შეიყვანე რიცხვი: "))

if (number > 100) {
    console.log("Large positive number")
} else if (number > 0 && number < 100) {
    console.log("Small positive number")
} else if (number < 0 && number % 2 === 0) {
    console.log("Negative even number")
} else if (number < 0 && number % 2 !== 0) {
    console.log("Negative odd number")
} else if (number === 0) {
    console.log("Zero")
}

if (number >= 10 && number <= 20) {
    console.log("Special range")
}