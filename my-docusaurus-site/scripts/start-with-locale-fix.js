// Wrapper script to fix locale issues before starting Docusaurus
require('./fix-locale.js');

// Now run the docusaurus start command with the locale fix applied
const { spawn } = require('child_process');
const path = require('path');

// Use npx to run docusaurus directly - this is more reliable than calling the binary directly
const args = ['docusaurus', 'start', ...process.argv.slice(2)];

const child = spawn('npx', args, {
  stdio: 'inherit',
  shell: true,
  env: {
    ...process.env,
    // Apply the locale fix by setting environment variables if needed
  }
});

child.on('close', (code) => {
  process.exit(code || 0);
});

child.on('error', (err) => {
  console.error('Error starting Docusaurus:', err);
  process.exit(1);
});

