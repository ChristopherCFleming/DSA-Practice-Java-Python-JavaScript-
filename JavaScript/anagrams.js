// anagrams
// Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

// test_00:
// anagrams('restful', 'fluster'); // -> true
// test_01:
// anagrams('cats', 'tocs'); // -> false
// test_02:
// anagrams('monkeyswrite', 'newyorktimes'); // -> true
// test_03:
// anagrams('paper', 'reapa'); // -> false
// test_04:
// anagrams('elbow', 'below'); // -> true
// test_05:
// anagrams('tax', 'taxi'); // -> false
// test_06:
// anagrams('taxi', 'tax'); // -> false
// test_07:
// anagrams('night', 'thing'); // -> true
// test_08:
// anagrams('abbc', 'aabc'); // -> false
// test_09:
// anagrams('po', 'popp'); // -> false
// test_10:
// anagrams('pp', 'oo') // -> false

// const anagrams = (s1, s2) => {
//   const count = {};
  
//   for (let char of s1) {
//     if (!(count[char])) {
//       count[char] = 0;
//     }
    
//     count[char] += 1
//   }
  
//   for (let char of s2) {
//     if (!(count[char])) {
//       return false;
//     }
//     count[char] -= 1;
//   }
  
//   for (let key in count) {
//     if (count[key] !== 0) {
//       return false
//     }
//   }
//   return true
// };

// Another solution using helper function:

const objectMaker = (s) => {
  let obj = {}
  for (char of s) {
    if (obj[char]) {
      obj[char] += 1;
    } else {
      obj[char] = 1;
    }
  }
  return obj;
}

const anagrams = (s1, s2) => {
  let firstOne = objectMaker(s1);
  
  for (char of s2) {
    if (!firstOne[char]) {
      return false
    } else {
      firstOne[char] -= 1;
    }
  }
  const counts = Object.values(firstOne);
  console.log(counts);
  for (num of counts) {
    if (num !== 0) {
      return false;
    }
  }
  return true;
};