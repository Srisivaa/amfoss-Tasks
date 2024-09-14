const fs = require('fs');

// Read from input.txt and write to output.txt
fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) throw err;
    fs.writeFile('output.txt', data, err => {
        if (err) throw err;
    });
});
