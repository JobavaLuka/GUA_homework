let input = "   Hello!!! My name is Goga!!! I love JS!!!   ";

let trimmed = input.trim();
let removed = trimmed.replaceAll("!!!", "!");
let dots = removed.slice(0, 20);
let result = dots + "...";

console.log(result);