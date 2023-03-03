const randomNum = Math.floor(Math.random() * 100) +1;
console.log(randomNum)

document.getElementById('btn').onclick = function() {
    const guess = document.getElementById('guess').value;
    console.log(guess)
    if (Number(guess) === randomNum) {
        alert('Congrats!')    
    } else if (Number(guess) > randomNum){
        alert("guess is too high");
    } else {
        alert('guess is too low');
    }
}