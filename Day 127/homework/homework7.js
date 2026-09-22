let text = prompt("შეიყვანეთ ტექსტი: ").trim().toLowerCase()

if (text == "open sesame") {
    console.log("საიდუმლო კარი გაიღო")
} else if (text.startsWith("open")) {
    console.log("კოდი არასრულია")
} else if (text.startsWith("close")) {
    console.log("კარი დაიხურა")
} else if (text.length < 5) {
    console.log("ტექსტი ძალიან მოკლეა")
} else {
    console.log("უცნობი ბრძანება")
}