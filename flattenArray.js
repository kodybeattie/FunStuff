var nums = [[23,43],[23,[4,5,6,[39,84,[8,5,10]]],[39]],2,432,23,65,93,23];
var newNums = [];
function flatteningNestedArrays(toFlatten, flattened){
  $.each(toFlatten, function(index, value){
    if (!Array.isArray(value)){
      flattened.push(value);
    }else{
      flatteningNestedArrays(value, flattened)
    }
  })
}
console.log(newNums)
flatteningNestedArrays(nums, newNums)
console.log(newNums)
