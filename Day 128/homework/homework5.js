let name = "Goga"
let math = 85
let english = 90
let programming = 95

let average = (math + english + programming) / 3

if (math < 50 || english < 50 || programming < 50) {
    console.log("Failed")
} else if (math >= 90 && english >= 90 && programming >= 90) {
    console.log("Excellent student")
} else if (average >= 80 && math >= 70) {
    console.log("Very good student")
} else {
    console.log("Needs improvement")
}