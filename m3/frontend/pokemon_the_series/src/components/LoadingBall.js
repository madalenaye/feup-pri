import Image from "./Image";
import Pokeball from "../images/pokeball.png";
import { AnimatePresence,motion } from "framer-motion";
export default function LoadingBall({classList=[]}) {
  const classlist = [...classList]
  return (
    <AnimatePresence >
      <motion.div initial={{opacity:0}} animate={{opacity:1}} exit={{ opacity: 0 }} transition={{duration:0.6, ease:"easeInOut"}} className={classlist.join(' ')}>
        <Image classList={["w-1/6", "animate-spin","search-loading-icon"]} props={{ src: Pokeball, alt: "Pokeball loading" }} />
      </motion.div>
    </AnimatePresence>
  );
}
