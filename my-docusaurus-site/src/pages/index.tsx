import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';
import Banner from '@site/src/components/Banner';
import Stats from '@site/src/components/Stats';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroContent}>
          <Heading as="h1" className="hero__title header-underline">
            Physical AI & Humanoid Robotics
          </Heading>
          <p className="hero__subtitle">
            Master the convergence of artificial intelligence and robotics through our comprehensive 6-module curriculum
          </p>
          <div className={styles.buttons}>
            <Link
              className="button button--primary button--lg"
              to="/docs/physical-ai-humanoid-robotics/intro">
              Start Learning
            </Link>
            <Link
              className="button button--secondary button--lg margin-left--md"
              to="/docs/physical-ai-humanoid-robotics/physical-ai-humanoid-robotics">
              Explore Modules
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

const statsData = [
  {
    value: '6',
    label: 'Comprehensive Modules',
  },
  {
    value: '20+',
    label: 'Hours of Content',
  },
  {
    value: '100+',
    label: 'Concepts Covered',
  },
  {
    value: '∞',
    label: 'Possibilities',
  },
];

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Physical AI & Humanoid Robotics`}
      description="Comprehensive curriculum on Physical AI & Humanoid Robotics - From sensors and actuators to human-robot interaction">
      <HomepageHeader />
      <main>
        <Banner
          title="Welcome to the Future of Robotics Education"
          subtitle="Cutting-edge curriculum developed by industry experts">
          <p>Our comprehensive program bridges the gap between artificial intelligence and robotics, preparing you for the next generation of intelligent systems.</p>
        </Banner>

        <div className="container margin-vert--lg">
          <Stats title="Curriculum Overview" items={statsData} />
        </div>

        <HomepageFeatures />
      </main>
    </Layout>
  );
}
