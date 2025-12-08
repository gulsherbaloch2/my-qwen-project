import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Manual sidebar configuration for the Physical AI & Humanoid Robotics curriculum
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System',
      link: {
        type: 'doc',
        id: 'physical-ai-humanoid-robotics/module-1/introduction',
      },
      items: [
        'physical-ai-humanoid-robotics/module-1/introduction',
        'physical-ai-humanoid-robotics/module-1/robotic-sensors',
        'physical-ai-humanoid-robotics/module-1/robotic-actuators',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Robotic Brain',
      link: {
        type: 'doc',
        id: 'physical-ai-humanoid-robotics/module-2/introduction',
      },
      items: [
        'physical-ai-humanoid-robotics/module-2/introduction',
        'physical-ai-humanoid-robotics/module-2/machine-learning',
        'physical-ai-humanoid-robotics/module-2/ai-control-systems',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: Robotic Motion and Control',
      link: {
        type: 'doc',
        id: 'physical-ai-humanoid-robotics/module-3/introduction',
      },
      items: [
        'physical-ai-humanoid-robotics/module-3/introduction',
        'physical-ai-humanoid-robotics/module-3/kinematics',
        'physical-ai-humanoid-robotics/module-3/dynamics',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Perception and Sensing',
      link: {
        type: 'doc',
        id: 'physical-ai-humanoid-robotics/module-4/introduction',
      },
      items: [
        'physical-ai-humanoid-robotics/module-4/introduction',
        'physical-ai-humanoid-robotics/module-4/computer-vision',
        'physical-ai-humanoid-robotics/module-4/sensor-fusion',
      ],
    },
    {
      type: 'category',
      label: 'Module 5: Learning and Adaptation',
      link: {
        type: 'doc',
        id: 'physical-ai-humanoid-robotics/module-5/introduction',
      },
      items: [
        'physical-ai-humanoid-robotics/module-5/introduction',
        'physical-ai-humanoid-robotics/module-5/reinforcement-learning',
        'physical-ai-humanoid-robotics/module-5/imitation-learning',
      ],
    },
    {
      type: 'category',
      label: 'Module 6: Human-Robot Interaction',
      link: {
        type: 'doc',
        id: 'physical-ai-humanoid-robotics/module-6/introduction',
      },
      items: [
        'physical-ai-humanoid-robotics/module-6/introduction',
        'physical-ai-humanoid-robotics/module-6/social-robotics',
        'physical-ai-humanoid-robotics/module-6/safety-ethics',
      ],
    },
  ],
};

export default sidebars;
