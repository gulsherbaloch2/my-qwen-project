import React from 'react';
import clsx from 'clsx';
import styles from './Banner.module.css';

interface BannerProps {
  title: string;
  subtitle?: string;
  type?: 'primary' | 'secondary' | 'success' | 'warning' | 'danger';
  children?: React.ReactNode;
  className?: string;
}

const Banner: React.FC<BannerProps> = ({ title, subtitle, type = 'primary', children, className }) => {
  return (
    <div className={clsx(styles.banner, styles[`banner--${type}`], className)}>
      <div className={styles.bannerHeader}>
        <h2 className={styles.bannerTitle}>{title}</h2>
        {subtitle && <p className={styles.bannerSubtitle}>{subtitle}</p>}
      </div>
      {children && <div className={styles.bannerBody}>{children}</div>}
    </div>
  );
};

export default Banner;