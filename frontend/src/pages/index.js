import { Routes, Route } from 'react-router-dom';
import LoginScreen from "../components/Login";
import Landing from '../components/Landing';
import Signup from '../components/Signup';

const Home = () => {
    return (
        <Routes>
            {/* <Route path="/about" element={<About />} /> */}
            <Route path="/login" element={<LoginScreen />} />
            <Route path="/" element={<Landing />} />
        </Routes>
    );
};

export default Home;