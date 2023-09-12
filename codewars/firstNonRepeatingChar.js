function firstNonRepeatingLetter(s) {

    if (s === '') {
      return '';
    };
    
    let charObj = {};
    let arr1 = s.split('');
    let arr = [];
    for (let i=0; i<arr1.length; i++) {
      arr.push(arr1[i].toLowerCase());
    };
    
    for (let i=0; i<arr.length; i++) {
      // console.log(arr[i])
      if (Object.keys(charObj).includes(arr[i])) {
        charObj[arr[i]]++;
      } else {
        charObj[arr[i]] = 1;
      };
    };
  
    let myArr = [];
    let keys = Object.keys(charObj);
    
    for (let i=0; i<keys.length; i++) {
      if (charObj[keys[i]] === 1) {
        myArr.push(keys[i]);
      } ;
    };
  
    let oddman = myArr[0];
    for (let i=0; i<arr1.length; i++) {
      if (oddman === arr1[i].toLowerCase()){
        return arr1[i]
      }
    };
    return '';
  };
  
  console.log(firstNonRepeatingLetter('abab')) // 'a'
  console.log(firstNonRepeatingLetter('a')) // 'a'
  console.log(firstNonRepeatingLetter('stress')) // 't'
  console.log(firstNonRepeatingLetter('sTreSS')) // 'T'
  console.log(firstNonRepeatingLetter('moonmen')) // 'e'