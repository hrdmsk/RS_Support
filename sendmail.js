const { exec } = require('child_process');

// Create Outlook draft
function createOutlookDraft() {
    const email = document.getElementById('email').value;
    const server = document.getElementById('server').value;
    const subject = 'Server Information';
    const body = `Email: ${email}\nServer: ${server}`;
    
    const mailtoUrl = `mailto:${email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    
    exec(`start "" "${mailtoUrl}"`, (err) => {
        if (err) {
            console.error('Error opening Outlook', err);
        } else {
            console.log('Outlook draft created');
        }
    });
}

document.getElementById('create-draft').addEventListener('click', createOutlookDraft);