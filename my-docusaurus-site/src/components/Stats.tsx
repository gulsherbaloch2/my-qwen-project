import React from 'react';
import clsx from 'clsx';
import styles from './Stats.module.css';

interface StatItem {
  value: string;
  label: string;
  icon?: string;
}

interface StatsProps {
  title?: string;
  items: StatItem[];
  className?: string;
}

const Stats: React.FC<StatsProps> = ({ title, items, className }) => {
  return (
    <div className={clsx(styles.stats, className)}>
      {title && <h2 className={styles.statsTitle}>{title}</h2>}
      <div className={styles.statsGrid}>
        {items.map((item, index) => (
          <div key={index} className={styles.statItem}>
            <div className={styles.statValue}>{item.value}</div>
            <div className={styles.statLabel}>{item.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Stats;