import React from "react";

import styles from "./Hero.module.css";
import { getImageUrl } from "../../utils";

export const Hero = () => {
  return (
    <section className={styles.container}>
      <div className={styles.content}>
        <h1 className={styles.title}>Hello, I am Attulya</h1>
        <p className={styles.description}>
          I'm a full-stack developer with 2 years of experience using the MERN stack. 
          I have Analysis and Machine Learning Experience through Research. 
          Reach out to know more!
        </p>
        
        <div>
        <a href="mailto:guptaattulyapratap@gmail.com" className={styles.contactBtn}>
          Contact Me
        </a>

        <a href="https://drive.google.com/file/d/1mRsHDmDqh8DtFyq_FUO94hDJNg5uGYvL/view?usp=sharing" target="_blank" 
           rel="noopener noreferrer"className={styles.contactBtn}>
          Resume
        </a>

        </div>

      </div>
      <img
        src={getImageUrl("hero/heroIcon.png")}
        alt="Hero image of me"
        className={styles.heroImg}
      />
      <div className={styles.topBlur} />
      <div className={styles.bottomBlur} />
    </section>
  );
};
