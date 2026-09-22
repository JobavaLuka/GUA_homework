let code = "AB-12-CD-34";

let changed = code.replaceAll("-", "*");
let result = changed.slice(0, -2) + "##";

console.log(result);