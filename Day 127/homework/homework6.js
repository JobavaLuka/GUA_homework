let name = prompt("შეიყვანეთ თქვენი სახელი: ").trim()

if (name == "") {
    console.log("სახელი აუცილებელია")
} else if (name.length < 3) {
    console.log("სახელი ძალიან მოკლეა")
} else if (name.length > 12) {
    console.log("სახელი ძალიან გრძელია")
} else if (name.startsWith("admin")) {
    console.log("ადმინისტრატორის სახელის გამოყენება აკრძალულია")
} else {
    console.log("მომხმარებლის სახელი მიღებულია")
}