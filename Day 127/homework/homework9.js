let sentence = prompt("შეიყვანეთ წინადადება: ").trim()

if (sentence == "") {
    console.log("ტექსტი არ შეგიყვანია")
} else if (sentence.toLowerCase().startsWith("javascript")) {
    console.log("ეს ტექსტი JavaScript-ზეა")
} else if (sentence.length > 20) {
    console.log(sentence.slice(0, 10))
} else if (sentence.endsWith("!")) {
    console.log("ტექსტი ემოციურია")
} else if (sentence.endsWith("?")) {
    console.log("ეს შეკითხვაა")
} else if (sentence.includes("bad")) {
    console.log(sentence.replaceAll("bad", "good"))
} else {
    console.log(sentence.toUpperCase())
}