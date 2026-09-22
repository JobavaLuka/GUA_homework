let age = 20;
let isStudent = true;

age < 13 ? 
    console.log("Child") : 
    age >= 13 && age < 18 ? 
    console.log("Teenager") : 
    age >= 18 && isStudent ? 
    console.log("Student") : 
    console.log("Adult")