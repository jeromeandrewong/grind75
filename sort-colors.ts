function sortColors(arr: number[]): void {
  let i = 0;
  for (let j = 0; j < arr.length; j++) {
    if (arr[j] === 0) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
    }
  }
  let k = i;
  for (let m = 0; m < arr.length; m++) {
    if (arr[m] === 1) {
      [arr[k], arr[m]] = [arr[m], arr[k]];
      k++;
    }
  }
}
