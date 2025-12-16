// Fix for locale issues on Windows
// This script patches Intl.Locale.prototype.maximize to handle errors gracefully

if (typeof Intl !== 'undefined' && Intl.Locale && Intl.Locale.prototype) {
  const originalMaximize = Intl.Locale.prototype.maximize;
  
  // Patch maximize to handle errors gracefully
  Intl.Locale.prototype.maximize = function() {
    try {
      return originalMaximize.call(this);
    } catch (error) {
      // If maximize fails, return the locale itself or a safe fallback
      try {
        // Try to return a basic locale with just the language
        const lang = this.language || 'en';
        return new Intl.Locale(lang);
      } catch (e) {
        // Ultimate fallback to English
        return new Intl.Locale('en');
      }
    }
  };
}

// Set environment variables for locale on Windows
if (process.platform === 'win32') {
  process.env.LANG = 'en_US.UTF-8';
  process.env.LC_ALL = 'en_US.UTF-8';
  process.env.LC_CTYPE = 'en_US.UTF-8';
}

