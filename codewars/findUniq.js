function findUniq(arr) {

    //determine the reocurring number
      // compare first and second
        // if the same
          //reocurring is the first
        // else
          // compare first and last
          //if the same
            // return the second
      // loop to compare num[i] to reocurring
        //return odd number
    let reocurring = null;
    
    if (arr[0] === arr[1]) {
      reocurring = arr[0]
    } else {
      if (arr[0] === arr[arr.length-1]) {
        return arr[1]
      }
    }
  
    for (let i=0; i<arr.length; i++) {
      if (arr[i] !== reocurring) {
        return arr[i]
      }
    }
  }