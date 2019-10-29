/*Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/
function twoSum(arr, target){
  i = 0;
  while (i <= (arr.length-1)){
    j = i+1;
    while (j <= (arr.length-1)){
      if ((arr[i] + arr[j]) == target){
        return ([i,j]);
      }
      j++;
    }
    i++;
  }
}
console.log(twoSum([32,42,34,24,3,4],7));
