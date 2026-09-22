let score = 75;
let isPremium = true;

score < 50 ? 
    console.log("Beginner") : 
    score < 80 ? 
    console.log("Intermediate") : 
    score >= 80 && isPremium ? 
    console.log("Pro") : 
    console.log("Advanced")