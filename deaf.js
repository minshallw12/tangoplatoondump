const prompt=require("prompt-sync")({sigint:true}); 

function canHear (speech) {
    let cantHear = 'abcdefghijklmnopqrstuvwxyz'.split('');
    if (speech.length <1) {
        return false
    }
    speechArr = speech.split('')
    console.log(speechArr)
    if (speechArr.length>=1) {
        for (let i=0; i<speechArr.length; i++) {
            let char = speechArr[i];
            console.log(char)
            for (let j=0; j<cantHear.length; j++) {
                let letter = cantHear[j];
                if (letter == char) {
                    return false;
                }
            }}}
            return true;
}


function response(speech) {
    let cantHear = 'abcdefghijklmnopqrstuvwxyz'.split('');
    if (speech.length <1) {
        answer = prompt('WHAT?!\n');
        response(answer)
    }
    speechArr = speech.split('')
    console.log(speechArr)

    if (speech.length>=1) {
        for (let i=0; i<speechArr.length; i++) {
            let char = speechArr[i];
            console.log(char)
            for (let j=0; j<cantHear.length; j++) {
                let letter = cantHear[j];
                if (char == letter) {
                    answer = prompt('SPEAK UP KID!\n');
                    response(answer);
                } else {
                    answer = prompt('NO, NOT SINCE 1946!\n')
                    response(answer)
                }
            }
        }  
        response(answer)
    }
}

function deafGrandma() {
    let speech = prompt("HEY KID!\n");
    let heard = canHear(speech);
    if (heard == true) {
        if (heard == 'GOODBYE!') {
            let answer = prompt('LEAVING SO SOON? \n')
            if (answer == 'GOODBYE!') {
                return 'LATER, SKATER!'
            }
            response(speech)
        }
    }
    if (heard == false) {
        response(prompt('WHAT??\n'))
    }
}

console.log(deafGrandma())
//deafGrandma()