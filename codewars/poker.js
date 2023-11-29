const consolidateNums = (two, three) => {
    let hand = []
    let hand_dict = {}
    for (let i=0; i<3; i++) {
      hand.push(three[i])
    }
    
    for (let i=0; i<2; i++) {
      hand.push(two[i])
    }
    
    for (let i=0; i<5; i++) {
      if (hand_dict[hand[i]['val']] === undefined) {
        hand_dict[hand[i]['val']] = 1
      } else {
        hand_dict[hand[i]['val']]++
      }
    }
    
    return hand_dict
  }
  
  function isPair(hole, flop){
  
    const my_dict = consolidateNums(hole, flop)
    
    for (key of Object.keys(my_dict)) {
      if (my_dict[key] >=2) {
        return true
      }
    }
    return false
  }
  
  function isTwoPair(hole, flop) {
  
    let pairs = 0
    let my_dict = consolidateNums(hole, flop)
    
    for (key of Object.keys(my_dict)) {
      if (my_dict[key] >=2) {
        pairs++
      }
    }
    
    if (pairs >=2) {
      return true
    } else {
      return false
    }
    
  }
  
  function isSet(hole, flop) {
    //write code here
    const my_dict = consolidateNums(hole, flop)
    
    for (key of Object.keys(my_dict)) {
      if (my_dict[key] >=3) {
        return true
      }
    }
    return false
  }