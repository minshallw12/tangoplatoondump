function fibonacci(theNumber){
    if (theNumber === 0) {
        return 0
    }
    if (theNumber === 1 || theNumber === 2) {
        return 1
    }
    return fibonacci(theNumber-1) + fibonacci(theNumber-2)
}

console.log(fibonacci(3))
console.log(fibonacci(0))
console.log(fibonacci(1))
console.log(fibonacci(2))
console.log(fibonacci(5))
console.log(fibonacci(8))
console.log(fibonacci(31))