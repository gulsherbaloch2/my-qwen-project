import React from 'react';
import Layout from '@theme-original/Layout';
import ChatbotToggle from '../components/Chatbot/ChatbotToggle';

type LayoutProps = typeof Layout extends (props: infer P) => React.ReactElement ? P : never;

export default function CustomLayout(props: LayoutProps): React.ReactElement {
  return (
    <>
      <Layout {...props}>
        {props.children}
      </Layout>
      <ChatbotToggle />
    </>
  );
}