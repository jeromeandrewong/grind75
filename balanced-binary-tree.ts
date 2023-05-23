class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode, right?: TreeNode) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

type AnswerType = {
  isBalanced: boolean;
};
function isBalanced(root: TreeNode | null): boolean {
  let answer: AnswerType = { isBalanced: true };
  getDepth(root, answer);
  return answer.isBalanced;
}
function getDepth(root: TreeNode | null, answer: AnswerType): number {
  if (!root) return 0;
  const leftDepth = getDepth(root.left, answer);
  const rightDepth = getDepth(root.right, answer);
  if (Math.abs(leftDepth - rightDepth) > 1) {
    answer.isBalanced = false;
  }
  return Math.max(leftDepth + 1, rightDepth + 1);
}
