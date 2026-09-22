let text = "   JavaScript is GREAT!!! JavaScript is POWERFUL!!!   ";

let trimmed = text.trim();
let replaced1 = trimmed.replaceAll("JavaScript", "JS");
let replaced2 = replaced1.replaceAll("!!!", "!");
let removed = replaced2.slice(0, 30);
let result = removed + "...";

console.log(result);