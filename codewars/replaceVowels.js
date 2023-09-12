function vowel2index(str) {

    // initiate vowels
    // split str by character
    // loop thru array
      // if element is a vowel
        // push the position (not index)
      // else push the element
  
    const vowels = ['a','e','i','o','u']
  
    let arr = str.split('')
    let answer = []
    
    for (let i=0; i < arr.length; i++) {
  
      if (vowels.includes(arr[i].toLowerCase())) {
        answer.push(i+1)
      } else {
        answer.push(arr[i])
      }
    }
  
    return answer.join('')
    
    
  }
  
  console.log(vowel2index('Hello')) // 'H2ll5'