let phone = " +995-599-12-34-56 ";

let trimmed = phone.trim();
let removed = trimmed.replaceAll("-", "");
let result = removed.slice(-9);

console.log(result);