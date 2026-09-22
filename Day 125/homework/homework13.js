let email = "   goga.chalauri@gmail.com   ";

let trimmed = email.trim();
let the_name = trimmed.slice(0, 13);
let result = the_name.replace(".", "_");

console.log(result);