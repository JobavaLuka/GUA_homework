let password = prompt("შეიყვანე შენი პაროლი: ").trim()

if (password == "") {
    console.log("პაროლი არ შეგიყვანია")
} else if (password == "javascript123") {
    console.log("სწორი პაროლია")
} else {
    console.log("არასწორი პაროლი")
}