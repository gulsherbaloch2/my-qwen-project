import React from 'react';
import ChatbotToggle from '../Chatbot/ChatbotToggle';

interface Props {
  children: React.ReactNode;
}

const ChatbotLayout: React.FC<Props> = ({ children }) => {
  return (
    <>
      {children}
      <ChatbotToggle />
    </>
  );
};

export default ChatbotLayout;