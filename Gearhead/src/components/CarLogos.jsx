import PropTypes from "prop-types";
import "./CarLogos.css";

const CarLogos = ({ className = "" }) => {
  return (
    <section className={`car-logos ${className}`}>
      <div className="logo-items-parent">
        <div className="logo-items">
          <img
            className="range-rover-1-icon"
            loading="lazy"
            alt=""
            src="/rangerover-1.svg"
          />
        </div>
        <div className="logo-items1">
          <img
            className="bmw-logo-1-icon"
            loading="lazy"
            alt=""
            src="/bmwlogo-1.svg"
          />
        </div>
        <div className="logo-items2">
          <img className="group-icon1" alt="" src="/group-11.svg" />
          <img
            className="vector-icon1"
            loading="lazy"
            alt=""
            src="/vector.svg"
          />
        </div>
        <div className="logo-items3">
          <img
            className="mercedes-amg-logo-1-icon"
            loading="lazy"
            alt=""
            src="/mercedesamglogo-1.svg"
          />
        </div>
        <div className="logo-items4">
          <img
            className="maserati-5-1-icon"
            loading="lazy"
            alt=""
            src="/maserati5-1.svg"
          />
        </div>
        <div className="logo-items5">
          <img
            className="subaru-12-1-icon"
            loading="lazy"
            alt=""
            src="/subaru12-1.svg"
          />
        </div>
        <div className="logo-items6">
          <img
            className="audi-1-1-icon"
            loading="lazy"
            alt=""
            src="/audi1-1.svg"
          />
        </div>
      </div>
    </section>
  );
};

CarLogos.propTypes = {
  className: PropTypes.string,
};

export default CarLogos;
