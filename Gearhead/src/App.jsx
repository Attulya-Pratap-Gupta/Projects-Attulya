import { useEffect } from "react";
import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import LandingUI4UpdateVersion from "./pages/LandingUI4UpdateVersion";
import ContactForm from "./components/ContactForm";
import SmoothScroll from "./SmoothScroll";

function App() {
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <>
      <SmoothScroll />
      <Routes>
        <Route path="/" element={<LandingUI4UpdateVersion />} />
        <Route path="/contact" element={<ContactForm />} />
      </Routes>
    </>
  );
}

export default App;
