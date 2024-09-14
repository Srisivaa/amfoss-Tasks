```javascript
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const printDiamond = (n) => {
  for (let i = 0; i < n; i++) {
    console.log(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
  }
  for (let i = n - 2; i >= 0; i--) {
    console.log(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
  }
};

rl.question('Enter a number: ', (answer) => {
  const n = parseInt(answer);
  printDiamond(n);
  rl.close();
});
``