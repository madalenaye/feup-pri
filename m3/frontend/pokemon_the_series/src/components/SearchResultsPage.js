import { useLocation } from "react-router-dom";
import { useState } from "react"
import Video from "./Video";
import Image from "./Image";
import backGroundLoop from "../videos/backgroundLoop.mp4";
import badge from "../images/badge.webp";
import Pokeball from "../images/pokeball.png"
import KantoBadges from "../images/kanto-badges.png"
import JohtoBadges from "../images/johto-badges.png"
import HoennBadges from "../images/hoenn-badges.webp"
import KalosBadges from "../images/kalos-badges.webp"

export default function SearchResultsPage() {
  const location = useLocation();
  const [hoveredDoc, setHoveredDoc] = useState(null);
  const { docs } = location.state;
  let rank = 0;

  const handleMouseEnter = (doc) => {
    setHoveredDoc(doc);
  };
  const determineRegionBadges = (doc)=>{
    const id = doc.id;
    console.log(id)
    const season = id.substring(0,2);
    switch(season){
      case "EP":
        const chosen = Math.random();
        if(chosen <=0.3){
          return KantoBadges;

        }
        else if(chosen >=0.6){
          return JohtoBadges;
        }
        else{
          return KalosBadges;
        }
      case "AG":
        return HoennBadges;
      default:
        return KantoBadges;
    }
  }
  
  const badgeProps = {
    src:badge,
    id:"header-logo",
    alt:"Badge logo"
  }
  const itemLogoProps = {
    src:Pokeball,
    alt:"Pokeball logo for the list items"
  }
  
  return (
    <div className="main-menu h-screen">
        <Video src={backGroundLoop} ariaLabel="Background video blue with a rotating pokeball symbol" classList={["opacity-80", "-z-10" ,"absolute","video-background"]}/>
        <div className="top-bar flex-row content-center justify-items-end">
            <Image props={badgeProps} classList={["select"]}/>
        </div>
        <div className="main-menu-content pokedex-results">
            {hoveredDoc && (
              <Image props={{src:determineRegionBadges(hoveredDoc)}} classList={["pokedex-images"]}/>
            )}
            {hoveredDoc && (
                <div className="pokedex-title">{hoveredDoc.title}</div>

            )}
            {hoveredDoc&&(
            <div className="pokedex-description"> {hoveredDoc.plot}</div>

            )}
            <div className="pokedex-items-list-container">
               <ul className="pokedex-items-list">
               {
                  docs.map((doc)=>{
                    rank++;
                    return (
                      <li className="pokedex-items-list-item"  key={doc.id} onMouseEnter={() => handleMouseEnter(doc)}>
                          <Image props={itemLogoProps} classList={["pokedex-items-list-item-logo"]}/>
                          <div className="pokedex-items-list-item-score">{doc.id}</div>
                          <div className="pokedex-items-list-item-title">{doc.title}</div>
                      </li>
                    );
                  })
                }
               </ul>
            </div>
        </div>
        <footer className="footer">
            <h1>All rights reserved</h1>
        </footer>
      </div>
  );
}
