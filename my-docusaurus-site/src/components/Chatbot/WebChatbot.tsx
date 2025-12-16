import React, { useState, useEffect, useRef } from 'react';
import './Chatbot.css';

type Message = {
  id: string;
  role: 'user' | 'assistant';
  content: string;
};

type ChatbotProps = {
  isOpen: boolean;
  onClose: () => void;
};

const WebChatbot: React.FC<ChatbotProps> = ({ isOpen, onClose }) => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      role: 'assistant',
      content: 'Hello! I\'m your AI assistant for the Physical AI & Humanoid Robotics curriculum. How can I help you today?'
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: inputValue.trim(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the backend API to get a response
      const response = await callBackendAPI(inputValue.trim());

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: response,
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 2).toString(),
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  // Function to call backend API
  const callBackendAPI = async (input: string): Promise<string> => {
    try {
      // For development, use the backend server (FastAPI on port 8000)
      // For production, you may need to adjust the URL
      // Using window object instead of process.env to avoid 'process is not defined' error in browser
      const API_BASE_URL = typeof window !== 'undefined'
        ? ((window as any).__SECRET_DOCUSAURUS_CONFIG__?.customFields?.apiBaseUrl as string)
        || (window as any).REACT_APP_API_BASE_URL
        || 'http://localhost:8000'
        : 'http://localhost:8000';

      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });

      if (!response.ok) {
        // Try to get error details from response
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data.response || data.answer || 'No response received';
    } catch (error) {
      console.error('Error calling backend API:', error);
      if (error instanceof TypeError && error.message.includes('fetch')) {
        return 'Failed to connect to the AI backend. Please make sure the backend service is running.';
      }
      return `Sorry, I encountered an error: ${error instanceof Error ? error.message : 'Unknown error'}`;
    }
  };

  if (!isOpen) return null;

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <div className="chatbot-title">AI Assistant</div>
        <button className="chatbot-close-btn" onClick={onClose}>
          ×
        </button>
      </div>
      <div className="chatbot-messages">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`chatbot-message ${message.role}`}
          >
            <div className="chatbot-message-content">
              {message.content.split('\n').map((line, i) => (
                <div key={i}>{line}</div>
              ))}
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="chatbot-message assistant">
            <div className="chatbot-message-content">
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSubmit} className="chatbot-input-form">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your message..."
          className="chatbot-input"
          disabled={isLoading}
        />
        <button
          type="submit"
          className="chatbot-send-btn"
          disabled={isLoading || !inputValue.trim()}
        >
          Send
        </button>
      </form>
    </div>
  );
};

export default WebChatbot;