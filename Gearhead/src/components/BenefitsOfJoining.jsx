import BenefitItems from "./BenefitItems";
import PropTypes from "prop-types";
import "./BenefitsOfJoining.css";

const BenefitsOfJoining = ({ className = "" }) => {
  return (
    <section className={`benefits-of-joining ${className}`}>
      <div className="benefits-graphics">
        <div className="benefits-graphics-child" />
        <div className="benefits-graphics-item" />
        <img className="pattern-icon" alt="" src="/pattern.svg" />
      </div>
      <div className="benefits-of-joining-parent">
        <b className="benefits-of-joining1">Benefits of Joining</b>
        <h1 className="why-join-gearhead-container">
          {`Why Join Gearhead `}
          <span className="mgmt">Mgmt</span>?
        </h1>
      </div>
      <div className="benefits-list">
        <BenefitItems
          benefitIcons="01"
          increasedExposure="Increased Exposure"
          reachAWiderAudiencePassio="Reach a wider audience passionate about automotive content."
        />
        <BenefitItems
          benefitIcons="02"
          increasedExposure="Community Access"
          reachAWiderAudiencePassio="Connect with like-minded creators and industry professionals."
        />
        <BenefitItems
          benefitIcons="03"
          increasedExposure="Enhanced Production"
          reachAWiderAudiencePassio="Gain access to resources and tools to elevate your content."
        />
        <BenefitItems
          benefitIcons="04"
          increasedExposure="Financial Opportunities"
          reachAWiderAudiencePassio="Unlock more ad revenue and monetization options."
        />
      </div>
    </section>
  );
};

BenefitsOfJoining.propTypes = {
  className: PropTypes.string,
};

export default BenefitsOfJoining;
