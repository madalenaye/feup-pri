
import Eevee from "../images/eevee.png"
import {useState} from "react";

export default function Tips({classList=[]}){
    const classlist = [...classList];
    const [tipId,setTipId] = useState(0);
    const numTips = 2;
    function clickHandler(){
        setTipId((tipId+1)%numTips);
    }

    switch(tipId){
        case 0:
            return(
                <div className={classlist.join(" ") + " bg-red-100 tip-item"} onClick={clickHandler}>
                    <h1>ola</h1>
                    <img src={Eevee} className="tip-image" alt="Eevee giving thumbs up in the corner"/>
                </div>
            );
        case 1:
            return(
                <div className={classList.join(" ") + " bg-yellow-100 tip-item"} onClick={clickHandler}>
                    <h1>adeus</h1>

                    <img src={Eevee} className="tip-image" alt="Eevee giving thumbs up in the corner"/>
                </div>
            )
        default:
            return;
    }

}
  