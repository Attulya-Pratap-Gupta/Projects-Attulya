import PropTypes from "prop-types";
import { useEffect, useRef } from "react";
import "./AboutUs.css";

const AboutUs = ({ className = "" }) => {
  const sectionRef = useRef(null);

  useEffect(() => {
    const section = sectionRef.current;
    const handleIntersection = (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
        } else {
          entry.target.classList.remove("in-view");
        }
      });
    };

    const observer = new IntersectionObserver(handleIntersection, {
      threshold: 0.1,
    });

    if (section) {
      observer.observe(section);
    }

    return () => {
      if (section) {
        observer.unobserve(section);
      }
    };
  }, []);

  return (
    <section ref={sectionRef} className={`about-us ${className}`}>
      <div className="about-content">
        <div className="about-gearhead-mgmt-parent">
          <h1 className="about-gearhead-mgmt">
            <p className="about">About</p>
            <p className="gearhead-mgmt">Gearhead Mgmt</p>
          </h1>
          <b className="gearhead-mgmt-is">
            Gearhead Mgmt is a network dedicated to supporting automotive
            content creators of all kinds. Whether you’re into classic cars,
            cutting-edge racing, or DIY mechanics, our platform offers
            unparalleled opportunities to grow your audience and enhance your
            content.
          </b>
          <a href="#contact-form" className="component-31">
            <img className="frame-icon3" alt="" src="/frame.svg" />
            <b className="youtube1">Join now</b>
          </a>
        </div>
        <div className="about-image">
          <img
            className="about-image-placeholder"
            loading="lazy"
            alt=""
            src="/rectangle-11@2x.png"
          />
        </div>
      </div>
    </section>
  );
};

AboutUs.propTypes = {
  className: PropTypes.string,
};

export default AboutUs;
