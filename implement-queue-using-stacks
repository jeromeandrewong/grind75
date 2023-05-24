class MyQueue {
  stack: number[] = [];
  tmpStack?: number[] = [];
  startIdx: number = 0;
  constructor() {}

  push(x: number): void {
    this.stack.push(x);
  }

  pop(): number | undefined {
    this.tmpStack?.push(this.stack[this.startIdx]);
    delete this.stack[this.startIdx];
    this.startIdx++;
    return this.tmpStack?.pop();
  }

  peek(): number {
    return this.stack[this.startIdx];
  }

  empty(): boolean {
    return this.stack.length - this.startIdx === 0;
  }
}
