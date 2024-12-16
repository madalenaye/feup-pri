import { useLocation } from "react-router-dom";
import WelcomePage from "./WelcomePage";
import MainMenu from "./MainMenu";
import ContentPage from "./ContentPage";
import SearchResultsPage from "./SearchResultsPage";
import { AnimatePresence ,motion} from "framer-motion";
import { Routes, Route } from "react-router";
export default function Navigator(){
    let location = useLocation()
    return(
            <AnimatePresence mode="wait">
                <Routes location={location} key={location.pathname}>
                    <Route path="/" element={<WelcomePage/>} />
                    <Route path="/mainmenu" element={
                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                            <MainMenu />
                        </motion.div>
                        } />
                    <Route path="/searchresults" element={
                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                            <SearchResultsPage />
                        </motion.div>
                        }/>
                    <Route path="/document" element={
                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                            <ContentPage />
                        </motion.div>
                        }/>
                </Routes>
            </AnimatePresence>
    );
};