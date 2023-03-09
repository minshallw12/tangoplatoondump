document.querySelector('button').addEventListener('click', getRandomPoke);


let counter = 1;
let page_type = ''

function getRandomPoke() {
    const randomizer = Math.floor(Math.random() * 151 + 1)
    console.log(randomizer)
     if (counter === 1) {
        axios
            .get(`https://pokeapi.co/api/v2/pokemon/${randomizer}`)
            .then((response) => {
            page_type = response.data.types[0].type.name;
            let pic = `<img src="${response.data.sprites.front_default}">`;
            console.log(pic)
            document.querySelector('#typedisplay').innerText = page_type;
            document.querySelector('#slot1').innerHTML = pic;
            counter += 1;
            console.log(counter)
        })
        .catch((error) => {
            console.log("no good 1: ", error);
        });
    } else {
        axios
        .get(`https://pokeapi.co/api/v2/pokemon/${randomizer}`)
        .then((response) => {
            let type = response.data.types[0].type.name;
            if (type === page_type) {
                let pic = `<img src="${response.data.sprites.front_default}">`;
                console.log(pic)
                document.querySelector('#typedisplay').innerText = type;
                document.querySelector(`#slot${counter}`).innerHTML = pic;
                counter += 1;
                console.log(counter)
            } else {
                return getRandomPoke()
            }
        })
        .catch((error) => {
            console.log("no good: ", error);
        });
    }
   
    

}


// Puesdocode
// Click the button
    //if there is no pokemon in slot 1 then 
        //fetch a random pokemon and display its front image in block 1
        //save the pokemon type for later queries
    //else
        //identify the type of pokemon in type section
        //fetch a random pokemon and display its front image in the next spaceblock 
