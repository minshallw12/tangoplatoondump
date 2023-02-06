const prompt=require("prompt-sync")({sigint:true}); 

function deafGrandma() {
    let speech = prompt("HEY KID!");
    let cantHear = 'abcdefghijklmnopqrstuvwxyz'.split('');
    if (speech == '') {
         'WHAT?!';
    }
    speechArr = speech.split('')
    for (let i=0; i<speechArr.length; i++) {
        let char = speechArr[i];
        if (char in cantHear) {
            return 'SPEAK UP KID!'
        }
    }   
}

deafGrandma()