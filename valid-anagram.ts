function isAnagram(s: string, t: string): boolean {
  // solution 1: hashmap
  let map = {};
  if (s.length !== t.length) return false;
  for (let char of s) {
    if (!map[char]) return false;
    else map[char]++;
  }
  for (let char of t) {
    if (!map[char]) return false;
    else {
      map[char]--;
      if (map[char] === 0) delete map[char];
    }
  }
  return Object.keys(map).length === 0;

  // solution 2: string
  // return s.split('').sort().join() ===t.split('').sort().join()
}
