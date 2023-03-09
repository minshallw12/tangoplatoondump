function factorial(num) {
    if (num < 1) {
        return 'bad input'
    }
    if (num === 1) {
        return 1
    }
    return num * factorial(num-1)
}

console.log(factorial(4))
console.log(factorial(7))
console.log(factorial(8))
console.log(factorial(1))
console.log(factorial(0))