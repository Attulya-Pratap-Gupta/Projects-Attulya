import PropTypes from "prop-types";
import "./Footer.css";

const Footer = ({ className = "" }) => {
  return (
    <footer className={`footer ${className}`}>
      <div className="join-the-gearhead-mgmt-network-parent">
        <h1 className="join-the-gearhead-container">
          <p className="join-the">{`Join the `}</p>
          <p className="gearhead-mgmt-network">
            {`Gearhead `}
            <span className="mgmt1">Mgmt</span> Network
          </p>
        </h1>
        <div className="y-t-footer">
          <div className="video-promo">
            <a href="mailto:sean@gearheadmgmt.com" className="component-3">
              <b className="youtube">Send a message</b>
            </a>
          </div>
        </div>
      </div>
      <div className="middle">
        <div className="footer-divider" />
        <div className="disclaimer-parent">
          <div className="disclaimer">Disclaimer</div>
          <img className="vector-icon2" alt="" src="/vector-1.svg" />
        </div>
      </div>
      <div className="footer-right">
        <div className="social-icons">
          <img
            className="social-icons-child"
            loading="lazy"
            alt=""
            src="/group-1-1.svg"
          />
          <div className="group-container">
            <img
              className="group-icon2"
              loading="lazy"
              alt=""
              src="/group.svg"
            />
          </div>
        </div>
        <div className="copyright">
          <b className="gearhead-mgmt1">© 2024 — Gearhead Mgmt</b>
        </div>
        <div className="spacer">
          <div className="double-spacer">
            <img
              className="spacer-items-icon"
              loading="lazy"
              alt=""
              src="/frame-2.svg"
            />
            <img
              className="spacer-items-icon1"
              loading="lazy"
              alt=""
              src="/frame-3.svg"
            />
          </div>
        </div>
      </div>
      <div className="footer-deco">
        <img className="vector-icon3" alt="" src="/vector-2.svg" />
        <div className="footer-deco-child" />
        <div className="footer-deco-item" />
      </div>
    </footer>
  );
};

Footer.propTypes = {
  className: PropTypes.string,
};

export default Footer;
