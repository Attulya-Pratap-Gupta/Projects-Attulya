import PropTypes from "prop-types";
import { useState, useRef, useEffect } from "react";
import "./Faq.css";

const Faq = ({ className = "" }) => {
  const [showAnswer1, setShowAnswer1] = useState(false);
  const [showAnswer2, setShowAnswer2] = useState(false);
  const [showAnswer3, setShowAnswer3] = useState(false);

  const toggleAnswer1 = () => setShowAnswer1(!showAnswer1);
  const toggleAnswer2 = () => setShowAnswer2(!showAnswer2);
  const toggleAnswer3 = () => setShowAnswer3(!showAnswer3);

  return (
    <section className={`faq ${className}`}>
      <div className="faq-graphic" />
      <h1 className="faqs">FAQ’s</h1>
      <div className="lorem-ipsum-dolor">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam.
      </div>
      <div className="lorem-ipsum-dolor1">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam.
      </div>
      <div className="faq-content">
        <div className="faq-list">
          <div className="faq-item">
            <div className="question" onClick={toggleAnswer1}>
              <b className="faq-question">How do I join Gearhead Mgmt?</b>
              <img
                className="faq-icon"
                alt=""
                src={showAnswer1 ? "/component-4-1.svg" : "/component-4-2.svg"}
              />
            </div>
            {showAnswer1 && (
              <div className="answer">
                Click the "Join Us" button and fill out the form to express your
                interest. We’ll get in touch with you shortly.
              </div>
            )}
          </div>
          <div className="faq-item">
            <div className="question" onClick={toggleAnswer2}>
              <b className="faq-question">What kind of support can I expect?</b>
              <img
                className="faq-icon"
                alt=""
                src={showAnswer2 ? "/component-4-1.svg" : "/component-4-2.svg"}
              />
            </div>
            {showAnswer2 && (
              <div className="answer">
                GearHead offers talent management services, including direct media advertising for unsold inventory, brand integrations with top automotive advertisers, and expert channel optimization.
              </div>
            )}
          </div>
          <div className="faq-item">
            <div className="question" onClick={toggleAnswer3}>
              <b className="faq-question">Is there a cost to join?</b>
              <img
                className="faq-icon"
                alt=""
                src={showAnswer3 ? "/component-4-1.svg" : "/component-4-2.svg"}
              />
            </div>
            {showAnswer3 && (
              <div className="answer">
                Joining GearHead is free! We help you monetize and grow, providing services that make you money, not cost you.
              </div>
            )}
          </div>
        </div>
      </div>
      <div className="faq-decoration">
        <div className="faq-bottom-graphic" />
        <img className="pattern-icon1" alt="" src="/pattern-1.svg" />
      </div>
    </section>
  );
};

Faq.propTypes = {
  className: PropTypes.string,
};

export default Faq;
