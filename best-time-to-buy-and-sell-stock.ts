function maxProfit(prices: number[]): number {
  let leftPointer = 0;
  let rightPointer = 1;
  let maxProfit = 0;
  while (rightPointer <= prices.length - 1) {
    if (prices[rightPointer] < prices[leftPointer]) {
      leftPointer = rightPointer;
      rightPointer++;
    } else {
      if (prices[rightPointer] - prices[leftPointer] > maxProfit) {
        maxProfit = prices[rightPointer] - prices[leftPointer];
      } else rightPointer++;
    }
  }
  return maxProfit;
}
