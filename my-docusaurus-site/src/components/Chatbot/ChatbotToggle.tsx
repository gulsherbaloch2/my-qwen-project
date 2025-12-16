import React, { useState } from 'react';
import WebChatbot from './WebChatbot';
import './ChatbotToggle.css';

const ChatbotToggle: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleChatbot = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      {!isOpen && (
        <button className="chatbot-toggle-btn" onClick={toggleChatbot}>
          <span className="chatbot-icon">💬</span>
        </button>
      )}
      <WebChatbot isOpen={isOpen} onClose={() => setIsOpen(false)} />
    </>
  );
};

export default ChatbotToggle;