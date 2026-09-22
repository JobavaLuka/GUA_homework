let username = "Goga"
let password = "Goa2026"
let age = 20

if (username === "" || password === "") {
    console.log("Fill in all fields")
} else if (username === "Goga" && password === "Goa2026") {
    console.log("Login successful")
} else if (username === "Goga" && password !== "Goa2026") {
    console.log("Incorrect password")
} else if (username !== "Goga") {
    console.log("Incorrect username")
}

if (age < 18) {
    console.log("Access denied")
}