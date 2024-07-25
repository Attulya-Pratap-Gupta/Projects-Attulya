import PropTypes from "prop-types";
import React from "react";
import "./Component.css";

const Component = ({
  className = "",
  label,
  placeholder,
  value,
  onChange,
  frameIcon,
  name,
}) => {
  return (
    <div className={`component-6 ${className}`}>
      <div className="link-labels">
        <b className="youtube-channel-link">{label}</b>
      </div>
      <div className="link-inputs">
        {frameIcon && <img className="frame-icon5" alt="" src="/frame2.svg" />}
        <input
          className="enter-youtube-channel"
          type="text"
          placeholder={placeholder}
          value={value}
          onChange={onChange}
          name={name}
        />
      </div>
    </div>
  );
};

Component.propTypes = {
  className: PropTypes.string,
  label: PropTypes.string,
  placeholder: PropTypes.string,
  value: PropTypes.string,
  onChange: PropTypes.func,
  frameIcon: PropTypes.bool,
  name: PropTypes.string,
};

export default Component;
