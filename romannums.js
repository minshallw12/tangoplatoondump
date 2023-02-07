function toRoman(arabicNum) {// # 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
    let output = [];// # 2. Create a OUTPUT string, set to ''
    let numeralMap = {
        "M":1000,
        "CM":900,
        "D":500,
        "CD":400,
        "C":100,
        "XC":90,
        "L":50,
        "XL":40,
        "X":10,
        "IX":9,
        "V":5,
        "IV":4,
        "I": 1
    }                 // # 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
    for (let i of Object.keys(numeralMap)) {// # 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
        let evenTimes = Math.floor(arabicNum/numeralMap[i]);
        arabicNum -= evenTimes * numeralMap[i]
        for (let j=0; j<evenTimes; j++){
            output.push(i)
        }  
    }
// # 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
// # 6. If EVENLY_DIVISIBLE_TIMES >= 1
//   # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
//   # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
// # 7. Return OUTPUT
    return output.join('')
}


console.log(toRoman(4))
console.log(toRoman(944))
console.log(toRoman(150))
console.log(toRoman(205))
console.log(toRoman(847))
console.log(toRoman(999))
console.log(toRoman(2999))