let email = prompt("შეიყვანეთ ელფოსტის მისამართი: ").trim().toLowerCase()

if (email == "admin@gmail.com") {
    console.log("ადმინისტრატორის ანგარიში")
} else if (email.endsWith("@gmail.com")) {
    console.log("Gmail-ის მომხმარებელი")
} else if (email.endsWith("@outlook.com")) {
    console.log("Outlook-ის მომხმარებელი")
} else {
    console.log("უცნობი ელფოსტის მისამართი")
}