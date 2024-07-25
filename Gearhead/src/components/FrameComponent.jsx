import PropTypes from "prop-types";
import "./FrameComponent.css";

const FrameComponent = ({ className = "" }) => {
  return (
    <section className={`hero-wrapper ${className}`}>
      <div className="hero">
        <video
          className="hero-background-video"
          autoPlay
          loop
          muted
          playsInline
        >
          <source src="/hero_video.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <div className="hero-content">
          <div className="overlay"></div>
          <header className="frame-parent">
            <div className="frame-group">
              <img
                className="frame-child"
                loading="lazy"
                alt=""
                src="/group-1.svg"
              />
              <div className="group-wrapper">
                <img
                  className="group-icon"
                  loading="lazy"
                  alt=""
                  src="/group.png"
                />
              </div>
            </div>
            <div className="hero-button">
              <img className="component-4-icon" alt="" src="/component-4.svg" />
            </div>
          </header>
          <h1 className="join-the-ultimate">
            Join the Ultimate Automotive Creator Network
          </h1>
        </div>
        <div className="video-promo">
          <a href="#contact-form" className="component-3">
            <img className="frame-icon2" alt="" src="/frame.svg" />
            <b className="youtube">Join us</b>
          </a>
          <div className="video-caption">
            <b className="fuel-your-passion">
              Fuel Your Passion for Automotive Content
            </b>
          </div>
        </div>
        <div className="join-us-wrapper">
          <b className="join-us">Join us</b>
        </div>
      </div>
    </section>
  );
};

FrameComponent.propTypes = {
  className: PropTypes.string,
};

export default FrameComponent;
