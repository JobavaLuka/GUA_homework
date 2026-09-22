let text = "I like cats. Cats are cute. My cat is sleeping.";
let nex_text = text.replaceAll("cats", "dogs").replaceAll("Cats", "Dogs").replaceAll("cat", "dog");

console.log(nex_text);