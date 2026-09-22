let numbers = prompt("Enter random number: ");

if (numbers > 10 && numbers % 2 === 0) {
    console.log("good number")
} else {
    console.log("bad time")
}


let name = prompt("Enter your name: ");

if (name.length > 5 || name.startsWith("g")) {
    console.log("good name")
} else {
    console.log("bad name")
}