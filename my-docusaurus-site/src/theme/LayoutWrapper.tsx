import React from 'react';
import ChatbotToggle from '../components/Chatbot/ChatbotToggle';

interface Props {
  children: React.ReactNode;
}

const LayoutWrapper: React.FC<Props> = ({ children }) => {
  return (
    <>
      {children}
      <ChatbotToggle />
    </>
  );
};

export default LayoutWrapper;