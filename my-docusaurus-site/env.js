// Runtime environment configuration for Vercel deployment
// This will be injected into the browser to provide API URL

// Define the API base URL based on environment
const apiBaseUrl = typeof window !== 'undefined' 
  ? (window.VERCEL_ENV && window.VERCEL_ENV !== 'development' 
      ? window.location.origin.replace(window.location.hostname, `your-backend-url.onrender.com`) // Replace with your actual backend URL
      : process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000')
  : process.env.API_BASE_URL || 'http://localhost:8000';

// Export for use in Docusaurus config
if (typeof window !== 'undefined') {
  (window as any).REACT_APP_API_BASE_URL = apiBaseUrl;
}