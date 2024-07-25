import React, { useState } from "react";
import Component from "./Component";
import PropTypes from "prop-types";
import "./ContactForm.css";
import emailjs from "emailjs-com";

const ContactForm = ({ className = "" }) => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    youtubeChannelLink: "",
    description: "",
  });

  const [errorMessage, setErrorMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!validateEmail(formData.email)) {
      setErrorMessage("Invalid email address. Please enter a valid email.");
      return;
    }

    const templateParams = {
      subject: `New Gearhead Request by ${formData.name}`,
      content: `FullName: ${formData.name}\n\nEmail: ${formData.email}\n\nYoutube: ${formData.youtubeChannelLink}\n\nDescription: ${formData.description}`,
      to_email: "sean@gearheadmgmt.com",
    };

    emailjs
      .send(
        "service_9b4jcgi",
        "template_7cm3m8n",
        templateParams,
        "76BtYn8aPjPa9Qh9y"
      )
      .then(
        (result) => {
          console.log(result.text);
          setErrorMessage("Form submitted successfully!");
          setFormData({
            name: "",
            email: "",
            youtubeChannelLink: "",
            description: "",
          });
        },
        (error) => {
          console.log(error.text);
          setErrorMessage("An error occurred. Please try again.");
        }
      );
  };

  return (
    <section id="contact-form" className={`contact-form ${className}`}>
      <img className="pattern-icon2" alt="" src="/pattern-2.svg" />
      <div className="contact-content">
        <div className="form-heading">
          <h1 className="join-now">Join Now</h1>
          <b className="provide-a-simple">
            Provide a simple description of your content here:
          </b>
        </div>
      </div>
      <div className="contact-content">
        <form className="contact-form1" onSubmit={handleSubmit}>
          <div className="form-fields">
            <div className="link-field">
              <Component
                label="Full Name"
                placeholder="Enter Name"
                value={formData.name}
                onChange={handleChange}
                frameIcon={false}
                name="name"
              />
              <Component
                label="Email"
                placeholder="Enter Email"
                value={formData.email}
                onChange={handleChange}
                frameIcon={false}
                name="email"
              />
              <Component
                label="YouTube Channel Link"
                placeholder="Enter YouTube Channel Link"
                value={formData.youtubeChannelLink}
                onChange={handleChange}
                frameIcon
                name="youtubeChannelLink"
              />
              <Component
                label="A brief description of your content"
                placeholder="A brief description of your content..."
                value={formData.description}
                onChange={handleChange}
                frameIcon={false}
                name="description"
              />
            </div>
            <div className="component-32">
              <button type="submit" className="youtube2">
                Submit
              </button>
            </div>
          </div>
        </form>
        {errorMessage && (
          <p
            className={
              errorMessage === "Form submitted successfully!"
                ? "success-message"
                : "error-message"
            }
          >
            {errorMessage}
          </p>
        )}
      </div>
    </section>
  );
};

ContactForm.propTypes = {
  className: PropTypes.string,
};

export default ContactForm;
