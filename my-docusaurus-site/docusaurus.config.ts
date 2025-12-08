import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Master the convergence of artificial intelligence and robotics',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://gulsherbaloch2.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For Vercel deployment, using root path
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'gulsherbaloch2', // Usually your GitHub org/user name.
  projectName: 'hakathon1', // Usually your repo name.

  onBrokenLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/gulsherbaloch2/hakathon1/tree/001-new-feature/my-docusaurus-site/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: ['@docusaurus/theme-mermaid'],

  stylesheets: [
    {
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap',
      type: 'text/css',
      rel: 'stylesheet',
    },
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Robotics',
      logo: {
        alt: 'Physical AI & Humanoid Robotics Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Modules',
        },
        {
          to: '/docs/physical-ai-humanoid-robotics/physical-ai-humanoid-robotics',
          position: 'left',
          label: 'Curriculum',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/gulsherbaloch2/hakathon1',
          label: 'GitHub',
          position: 'right',
        },
      ],
      // Enable mobile sidebar toggle and responsive behavior
      hideOnScroll: false,
      style: 'primary',
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Curriculum',
          items: [
            {
              label: 'Module 1: Robotic Nervous System',
              to: '/docs/physical-ai-humanoid-robotics/module-1/introduction',
            },
            {
              label: 'Module 2: Robotic Brain',
              to: '/docs/physical-ai-humanoid-robotics/module-2/introduction',
            },
            {
              label: 'Module 3: Motion and Control',
              to: '/docs/physical-ai-humanoid-robotics/module-3/introduction',
            },
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/gulsherbaloch2/hakathon1',
            },
            {
              label: 'Documentation',
              to: '/docs/physical-ai-humanoid-robotics/intro',
            },
            {
              label: 'Blog',
              to: '/blog',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Curriculum. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
