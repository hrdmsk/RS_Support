const { ipcRenderer } = require('electron');
const fs = require('fs');

document.getElementById('save').addEventListener('click', () => {
    const email = document.getElementById('email').value;
    const server = document.getElementById('server').value;
    const data = `Email: ${email}\nServer: ${server}`;
    
    fs.writeFile('output.txt', data, (err) => {
        if (err) {
            console.error('Error writing file', err);
        } else {
            console.log('File saved successfully');
        }
    });
});