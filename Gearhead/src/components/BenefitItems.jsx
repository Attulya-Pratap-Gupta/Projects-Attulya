import PropTypes from "prop-types";
import "./BenefitItems.css";

const BenefitItems = ({
  className = "",
  benefitIcons,
  increasedExposure,
  reachAWiderAudiencePassio,
}) => {
  return (
    <div className={`benefit-items ${className}`}>
      <b className="benefit-icons">{benefitIcons}</b>
      <div className="benefit-descriptions">
        <b className="increased-exposure">{increasedExposure}</b>
        <b className="reach-a-wider">{reachAWiderAudiencePassio}</b>
      </div>
    </div>
  );
};

BenefitItems.propTypes = {
  className: PropTypes.string,
  benefitIcons: PropTypes.string,
  increasedExposure: PropTypes.string,
  reachAWiderAudiencePassio: PropTypes.string,
};

export default BenefitItems;
