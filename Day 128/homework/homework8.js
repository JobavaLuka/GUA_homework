let score1 = Number(prompt("შეიყვანე პირველი გამოცდის ქულა: "))
let score2 = Number(prompt("შეიყვანე მეორე გამოცდის ქულა: "))
let score3 = Number(prompt("შეიყვანე მესამე გამოცდის ქულა: "))
let age = Number(prompt("შეიყვანე შენი ასაკი: "))

let average = (score1 + score2 + score3) / 3

if (score1 < 0 || score1 > 100 || score2 < 0 || score2 > 100 || score3 < 0 || score3 > 100) {
    console.log("Invalid score")
} else if (score1 < 50 || score2 < 50 || score3 < 50) {
    console.log("Rejected")
} else if (score1 >= 90 && score2 >= 90 && score3 >= 90) {
    console.log("Scholarship candidate")
} else if (score1 >= 80 && score2 >= 80 && score3 >= 80 && age >= 18) {
    console.log("Accepted")
} else if (average >= 70 && (score1 < 80 || score2 < 80 || score3 < 80)) {
    console.log("Waitlisted")
} else {
    console.log("Not accepted")
}