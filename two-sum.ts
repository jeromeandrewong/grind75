function twoSum(nums: number[], target: number): number[] {
  let numberMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (numberMap.has(diff)) return [numberMap.get(diff), i];
    else numberMap.set(nums[i], i);
  }
  return [-1];
}
