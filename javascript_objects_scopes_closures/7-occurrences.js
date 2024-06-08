#!/usr/bin/node
// exports.nbOccurences = function (list, searchElement) {
//   let nOccurences = 0;
//     for (let i = 0; i < list.length; i++) {
//       if (searchElement === list[i]) {
//         nOccurences++;
//       }
//     }
//     return nOccurences;
// };

// // Consistent indentation (2 spaces)

function nbOccurences(list, searchElement) {
  let nOccurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurences++;
    }
  }
  return nOccurences;
}

// Modern export syntax (assuming module system)
module.exports = nbOccurences;
