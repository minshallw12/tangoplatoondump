export const isPangram = (phrase: string): boolean => {
    let lowercase:string = phrase.toLowerCase();
    let alphabet:string = 'abcdefghijklmnopqrstuvwxyz';
    let alphaArr: string[] = alphabet.split('');
    let obj: {[key:string]: number} = {};
    
    for (let i=0; i<lowercase.length; i++) {
  
      if (alphabet.includes(lowercase[i])) {
        if (obj.hasOwnProperty(lowercase[i])) {
          obj[lowercase[i]]++;
        } else {
          obj[lowercase[i]] = 1;
        };
      };
    };
  
    for (let i=0; i<alphaArr.length; i++) {
      if (!obj.hasOwnProperty(alphaArr[i])) {
        return false;
      };
    };
  
    return true;
  };