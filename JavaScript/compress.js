// compress
// Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

// 'aaa' compresses to '3a'
// 'cc' compresses to '2c'
// 't' should remain as 't'
// You can assume that the input only contains alphabetic characters.

// compress('ccaaatsss'); // -> '2c3at3s'
// compress('ssssbbz'); // -> '4s2bz'
// compress('ppoppppp'); // -> '2po5p'
// compress('nnneeeeeeeeeeeezz'); // -> '3n12e2z'
// compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'); 
// // -> '127y'


const compress = (s) => {
  let startOfRun = s[0];
  let endOfRun = s[0];
  let count = 0;
  let compressed = [];
  
  for (let i = 0; i < s.length; i++) {
    endOfRun = s[i];
    
    if (startOfRun == endOfRun) {
      count += 1;
    } else {
      if (count > 1) {
        compressed.push(count);
      }
      compressed.push(startOfRun);
      startOfRun = s[i];
      count = 1;
    }
  }
  if (count > 1) {
    compressed.push(count);
  }
  compressed.push(startOfRun);
  return compressed.join("");
};