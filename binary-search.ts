// Given an array of integers nums which is sorted in ascending order, and an integer target,
// write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;
  while (right - left) {
    const mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;
    else if (nums[mid] > target) right = mid - 1;
    else if (nums[mid] < target) left = mid + 1;
  }
  return -1;
}
