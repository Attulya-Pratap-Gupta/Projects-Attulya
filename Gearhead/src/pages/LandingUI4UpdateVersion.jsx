import FrameComponent from "../components/FrameComponent";
import CarLogos from "../components/CarLogos";
import AboutUs from "../components/AboutUs";
import BenefitsOfJoining from "../components/BenefitsOfJoining";
import Testimonial from "../components/Testimonial";
import Faq from "../components/Faq";
import ContactForm from "../components/ContactForm";
import Footer from "../components/Footer";
import "./LandingUI4UpdateVersion.css";

const LandingUI4UpdateVersion = () => {
  return (
    <div className="landing-ui-4-update-version">
      <FrameComponent />
      <img className="vector-icon" alt="" src="/vector.svg" />
      <CarLogos />
      <AboutUs />
      <BenefitsOfJoining />
      <Testimonial />
      <Faq />
      <ContactForm />
      <Footer />
    </div>
  );
};

export default LandingUI4UpdateVersion;
