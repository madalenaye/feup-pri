
import Eevee from "../images/eevee.png"
import Jolteon from "../images/jolteon.png"
import {useState} from "react";
import {motion,AnimatePresence} from "framer-motion"
export default function Tips({classList=[]}){
    const classlist = [...classList];
    const [tipId,setTipId] = useState(0);

    const numTips = 2;
    function clickHandler(){
        setTipId((tipId+1)%numTips);
    }
   
    return (
        <AnimatePresence>
          {tipId === 0 && (
            <motion.div key="tip0" initial={{ scale: 0 }} animate={{ scale: 1 }} exit={{ scale: 0 }} className={classlist.join(" ") + " bg-yellow-300 opacity-90"} onClick={clickHandler} >
              <h1 className="tip-intro">Did you know: Pokémon means 'Pocket Monsters'!</h1>
              <p className="tip-text">
                Pokémon is an abbreviation of 'Poketto Monsutā' which means 'Pocket Monster' in Japanese. Because they fit in your pocket, of course! Although luckily they live in Poke balls, imagine the mess if they used your pockets as a loo...
              </p>
              <img src={Jolteon} className="tip-image" alt="Eevee giving thumbs up in the corner" />
            </motion.div>
          )}
          {tipId === 1 && (
            <motion.div
              key="tip1"
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              exit={{ scale: 0 }}
              className={classlist.join(" ") + " bg-red-300 opacity-90"}
              onClick={clickHandler}
            >
              <h1 className="tip-intro">Did you know: Lots of Pokémon names are puns!</h1>
              <p className="tip-text">
                For example, the powers of Mimikyu are literally to 'mimic you'. And Sudowoodo? 'Psudo wood', or fake wood. Squirtle is a reference to the fact that he's a turtle who can squirt water, and Charmander is so-called because it's a fire Pokémon which can 'char' you. Which other clever names can you spot? 
                <a href="https://www.beano.com/random/fun/pokemon-facts" onClick={(e)=>{e.stopPropagation()}}> (source: https://www.beano.com/random/fun/pokemon-facts)</a>
                </p>
              
              <img src={Eevee} className="tip-image" alt="Eevee giving thumbs up in the corner" />
            </motion.div>
          )}
        </AnimatePresence>
      );

}
  