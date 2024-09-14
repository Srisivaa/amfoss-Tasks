```javascript
const fs = require('fs');

const printDiamond = (n) => {
    let lines = [];
    for (let i = 0; i < n; i++) {
        lines.push(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
    }
    for (let i = n - 2; i >= 0; i--) {
        lines.push(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
    }
    return lines.join('\n');
};

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) throw err;
    const n = parseInt(data.trim(), 10);
    const diamond = printDiamond(n);
    fs.writeFile('output.txt', diamond, (err) => {
        if (err) throw err;
    });
});
```