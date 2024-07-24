const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow(page) {
    const mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'pages', page, 'renderer.js'),
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile(path.join(__dirname, 'pages', page, 'index.html'));
}

app.whenReady().then(() => {
    createWindow('page1'); // デフォルトページ
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow('page1');
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});