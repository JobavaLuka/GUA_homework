let age = 19;
let hasTicket = true;
let isVip = false;

age < 18 ? 
    console.log("Too Young") : 
    age >= 18 && !hasTicket ? 
    console.log("No Ticket") : 
    hasTicket && isVip === true ? 
    console.log("VIP Entrance") : 
    console.log("Normal Entrance")