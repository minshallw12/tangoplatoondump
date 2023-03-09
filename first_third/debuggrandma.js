const prompt=require("prompt-sync")({sigint:true}); 

function deafgran(){
    let goodbyes = 0
    while (true) {
        let userinput = prompt("> ")
        if (userinput === "" ) {
            console.log("WHAT!?")
        }
        else if (userinput.toLowerCase() === userinput) {
            console.log("SPEAK UP, KID!")
        }
        else if (userinput === "GOODBYE!" ) {
            goodbyes++;
            if (goodbyes === 1 ) {
                console.log("LEAVING SO SOON?")
            }
            else if ( goodbyes === 2 ) {
                return "LATER, SKATER!"
            }
        }        
        else if (userinput.toUpperCase() === userinput ) {
            console.log('NO, NOT SINCE 1946!')
        }
    }
}

console.log(deafgran())