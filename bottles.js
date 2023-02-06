function bottles(num) {
    let i = num;
    while (i>1){
        console.log(`${i} bottles of beer on the wall, ${i} bottles of beer`);
        console.log(`Take one down and pass it around, ${i-1} bottles of beer on the wall.`);
        i--;
    }
    console.log('1 bottle of beer on the wall, 1 bottle of beer.')
    console.log('Take one down and pass it around, no more bottles of beer on the wall.')
    console.log('No more bottles of beer on the wall, no more bottles of beer.')
    console.log(`Go to the store and buy some more, ${num} bottles of beer on the wall.`)
}

bottles(99)