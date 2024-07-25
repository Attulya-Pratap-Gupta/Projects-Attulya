import PropTypes from "prop-types";
import { useState } from "react";
import "./Testimonial.css";

const testimonials = [
  {
    name: "Matt Zubrick",
    title: "Founder, 5 O'Clock Garage",
    quote:
      "Joining Gearhead Network has been a game-changer for me. I'm excited to go from zero YouTube presence to building a thriving channel with the guidance of their team of automotive experts. The future looks bright!",
    image: "/client_1.jpg",
  },
  {
    name: "Russell Richardson",
    title: "@RussFlipsWhips",
    quote:
      "I'm thrilled to join the Gearhead Network and can't wait to see what the future holds. Their expertise in connecting creators with top-tier advertisers and sponsors is exactly what I need to take my channel to the next level.",
    image: "/client_2.jpg",
  },
  {
    name: "Javuan Banks",
    title: "@javuanbanks",
    quote:
      "Being part of Gearhead Network is an exciting opportunity. I'm looking forward to forming valuable collaborations and partnerships within the automotive community, which will undoubtedly boost my channel's growth.",
    image: "/client_3.jpg",
  },
];

const Testimonial = ({ className = "" }) => {
  const [activeIndex, setActiveIndex] = useState(0);
  const [linePosition, setLinePosition] = useState(0);

  const handleButtonClick = (index) => {
    setActiveIndex(index);
    setLinePosition(index);
  };

  return (
    <section className={`testimonial ${className}`}>
      <div className="testimonial-content-container">
        {testimonials.map((testimonial, index) => (
          <div
            key={index}
            className={`testimonial-content ${
              index === activeIndex ? "active" : "hidden"
            }`}
          >
            <img
              className="image-icon"
              loading="lazy"
              alt=""
              src={testimonial.image}
            />
            <div className="testimonial-author">
              <div className="testimonial-author-child" />
              <b className="john-doe">{testimonial.name}</b>
              <b className="classic-car-enthusiast">{testimonial.title}</b>
            </div>
          </div>
        ))}
      </div>
      <div className="testimonial-quote-container">
        {testimonials.map((testimonial, index) => (
          <div
            key={index}
            className={`testimonial-quote ${
              index === activeIndex ? "active" : "hidden"
            }`}
          >
            <div className="quote-content">
              <div className="quote-paragraph-wrapper">
                <div className="quote-paragraph">
                  <div className="quotes-wrapper">
                    <img
                      className="quotes-icon"
                      loading="lazy"
                      alt=""
                      src="/quotes.svg"
                    />
                  </div>
                  <blockquote className="joining-gearhead-mgmt">
                    {testimonial.quote}
                  </blockquote>
                  <img
                    className="quotes-icon1"
                    loading="lazy"
                    alt=""
                    src="/quotes.svg"
                  />
                </div>
              </div>
            </div>
          </div>
        ))}
        <div className="quote-attribution">
          <div className="attribution-content">
            <b
              className={`attribution-placeholder ${
                activeIndex === 0 ? "active" : ""
              }`}
              onClick={() => handleButtonClick(0)}
            >
              01
            </b>
            <div className={`frame-container position-${linePosition}`}>
              {linePosition === 0 && (
                <div className="line-wrapper">
                  <div className="line" />
                </div>
              )}
              <b
                className={`b ${activeIndex === 1 ? "active" : ""}`}
                onClick={() => handleButtonClick(1)}
              >
                02
              </b>
              {linePosition === 1 && (
                <div className="line-wrapper">
                  <div className="line" />
                </div>
              )}
              <b
                className={`b1 ${activeIndex === 2 ? "active" : ""}`}
                onClick={() => handleButtonClick(2)}
              >
                03
              </b>
            </div>
            {linePosition === 2 && (
              <div className="line-wrapper">
                <div className="line" />
              </div>
            )}
          </div>
        </div>
      </div>
    </section>
  );
};

Testimonial.propTypes = {
  className: PropTypes.string,
};

export default Testimonial;
