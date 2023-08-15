export function cowboysDollars(boots: string[]): string {
    function countBoot(boot: string): number {
      let count: number = 0;
  
      for (let i = 0; i < boot.length - 4; i++) { // Adjusted loop length
        if (boot[i] === '&') {
          break;
        } else {
          if (
            boot[i] === '[' &&
            boot[i + 1] === '(' &&
            boot[i + 2] === '1' &&
            boot[i + 3] === ')' &&
            boot[i + 4] === ']'
          ) {
            count++;
            i += 4; // Skip the matched pattern
          }
        }
      }
      return count;
    }
  
    let left: number = countBoot(boots[0]);
    let right: number = countBoot(boots[1]);
    
    return `This Rhinestone Cowboy has ${right} dollar bills in his right boot and ${left} in the left`;
  }