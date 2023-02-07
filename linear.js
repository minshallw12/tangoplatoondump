function basicLinear(str, str2) {
    let arr = str2.split('');
    for (let i=0; i<arr.length; i++) {
        if (str === arr[i]) {
            return i
        }
    }
}

console.log(basicLinear('a', 'banana'))

function globalLinear(str, str2) {
    let data = []
    let arr = str2.split('');
    for (let i=0; i<arr.length; i++) {
        if (str === arr[i]) {
            data.push(i)
        }
    }
    return data
}

console.log(globalLinear('a', 'banana'))
console.log(globalLinear('n', 'banana'))
console.log(globalLinear('5', '15845321565184'))
console.log(globalLinear(' ', "How you doin'?"))
