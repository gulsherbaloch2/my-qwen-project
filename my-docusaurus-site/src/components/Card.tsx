import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import clsx from 'clsx';
import styles from './Card.module.css';

interface CardProps {
  title: string;
  description: string;
  icon?: string;
  link?: string;
  children?: React.ReactNode;
}

export const Card: React.FC<CardProps> = ({ title, description, icon, link, children }) => {
  const cardContent = (
    <div className={clsx('card', styles.card)}>
      <div className={styles.cardHeader}>
        {icon && <div className={styles.cardIcon}>{icon}</div>}
        <h3 className={styles.cardTitle}>{title}</h3>
      </div>
      <div className={styles.cardBody}>
        <p className={styles.cardDescription}>{description}</p>
        {children}
      </div>
    </div>
  );

  if (link) {
    return (
      <a href={useBaseUrl(link)} className={styles.cardLink}>
        {cardContent}
      </a>
    );
  }

  return cardContent;
};

interface ModuleCardProps {
  number: string;
  title: string;
  description: string;
  to: string;
}

export const ModuleCard: React.FC<ModuleCardProps> = ({ number, title, description, to }) => {
  return (
    <a href={useBaseUrl(to)} className={styles.moduleCardLink}>
      <div className={clsx('card', styles.moduleCard)}>
        <div className={styles.moduleCardHeader}>
          <div className={styles.moduleNumber}>
            <span>Module {number}</span>
          </div>
          <h3 className={styles.moduleTitle}>{title}</h3>
        </div>
        <div className={styles.moduleCardBody}>
          <p className={styles.moduleDescription}>{description}</p>
          <div className={styles.moduleCta}>Explore →</div>
        </div>
      </div>
    </a>
  );
};