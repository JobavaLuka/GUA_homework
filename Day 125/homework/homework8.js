let password = "Goga12345";

let part = password.slice(0, 2);
let cover = "*".repeat(password.length - 2);

let the_code = part + cover;

console.log(the_code);