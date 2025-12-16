# PowerShell script to start Docusaurus with proper locale settings on Windows
$env:LANG = "en_US.UTF-8"
$env:LC_ALL = "en_US.UTF-8"
$env:LC_CTYPE = "en_US.UTF-8"

# Start Docusaurus
npm run docusaurus start


