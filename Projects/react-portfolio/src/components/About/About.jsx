import React from "react";

import styles from "./About.module.css";
import { getImageUrl } from "../../utils";

export const About = () => {
  return (
    <section className={styles.container} id="about">
      <h2 className={styles.title}>About</h2>
      <div className={styles.content}>
        <img
          src={getImageUrl("about/aboutImage.png")}
          alt="Me sitting with a laptop"
          className={styles.aboutImage}
        />
        <ul className={styles.aboutItems}>
          <li className={styles.aboutItem}>
            <img src={getImageUrl("about/cursorFrontend.png")} alt="Cursor icon" />
            <div className={styles.aboutItemText}>
              <h3>Frontend Development</h3>
              <p>
                I'm a fullstack developer with experience in building responsive,
                optimized sites using HTML, CSS, JS and frameworks like React
              </p>
            </div>
          </li>
          <li className={styles.aboutItem}>
            <img src={getImageUrl("about/cursorBackend.png")} alt="Server icon" />
            <div className={styles.aboutItemText}>
              <h3>Backend Development</h3>
              <p>
                Experience developing fast and optimized backend systems. 
              </p>
            </div>
          </li>
          <li className={styles.aboutItem}>
            <img src={getImageUrl("about/dataScienceAnalysis.png")} alt="Data Science/Analysis icon" />
            <div className={styles.aboutItemText}>
              <h3>Data Science and ML Expertise</h3>
              <p>
                Experience as a Data Analyst and Data Scientist. Worked on NLP,
                Association Analysis, Reinforcement Learning and Transformer Models
              </p>
            </div>
          </li>
        </ul>
      </div>
    </section>
  );
};
