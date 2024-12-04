import { useLocation } from "react-router-dom";
import WelcomePage from "./WelcomePage";
import MainMenu from "./MainMenu";
import { AnimatePresence ,motion} from "framer-motion";
import { Routes, Route } from "react-router";
export default function Navigator(){
    let location = useLocation()
    return(
            <AnimatePresence mode="wait">
                <Routes location={location} key={location.pathname}>
                    <Route path="/" element={<WelcomePage/>} />
                    <Route path="/MainMenu" element={
                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                            <MainMenu />
                        </motion.div>
                        } />
                </Routes>
            </AnimatePresence>
    );
};