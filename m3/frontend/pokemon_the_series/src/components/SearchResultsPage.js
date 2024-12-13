import { useLocation } from "react-router-dom";
import { useState } from "react"
import Video from "./Video";
import Image from "./Image";
import backGroundLoop from "../videos/backgroundLoop.mp4";
import badge from "../images/badge.webp";
import Pokeball from "../images/pokeball.png";
import KantoBadges from "../images/kanto-badges.png";
import JohtoBadges from "../images/johto-badges.png";
import HoennBadges from "../images/hoenn-badges.webp";
import KalosBadges from "../images/kalos-badges.webp";
import SinnohBadges from "../images/sinnoh-badges.webp";
import UnovaBadges from "../images/unova-badges.png"
import Zcrystals from "../images/zcrystals.png"
import WildSearch from "../images/wildsearchresults.jpg"
import SearchResults from "../images/SearchResults.png";

export default function SearchResultsPage() {
  const location = useLocation();
  const [hoveredDoc, setHoveredDoc] = useState(null);
  const { docs } = location.state;
  let chosen = 0;
  const handleMouseEnter = (doc) => {
    setHoveredDoc(doc);
  };
  const determineRegionBadges = (doc)=>{
    const id = doc.id;
    const season = id.substring(0,2);
    switch(season){
      case "EP":
        chosen = Math.random();
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
        chosen = Math.random();
        
        if(chosen <= 0.5){
          return KantoBadges;
        }
        else{
          return HoennBadges;
        }
      case "DP":
        return SinnohBadges;
      case "BW":
        return UnovaBadges;
      case "XY":
        return KalosBadges;
      case "SM":
        return Zcrystals;
      default:
        return;
    }
  }
  const badgeClickHandler = ()=>{
    console.warn("clicked")
  }
  const badgeProps = {
    src:badge,
    id:"header-logo",
    alt:"Badge logo",
    onClick:badgeClickHandler
  }
  const itemLogoProps = {
    src:Pokeball,
    alt:"Pokeball logo for the list items"
  }
  const defaultProps = {
    src: WildSearch,
    alt:"Pokemon game scene where a wild pokemon appears with a Unown pokemon",

  }
  const SearchResultTitleProps ={
    src:SearchResults,
    alt:"Title for the page as Search results",
    className:"topbar-title"
  }
  
  return (
    <div className="main-menu h-screen">
        <Video src={backGroundLoop} ariaLabel="Background video blue with a rotating pokeball symbol" classList={["opacity-80", "-z-10" ,"absolute","video-background"]}/>
        <div className="top-bar">
            <Image props={badgeProps} classList={["select","topbar-icon"]}/>
            <Image props={SearchResultTitleProps}/>
        </div>
        <div className="main-menu-content pokedex-results">
            {
              hoveredDoc?
              <Image props={{src:determineRegionBadges(hoveredDoc)}} classList={["pokedex-images spin"]}/>
              :
              <Image props={defaultProps} classList={["pokedex-images"]}/>
            }
            {
              hoveredDoc? 
              (
                <div className="pokedex-text-box title">
                  <p className="pokedex-text-box-text title">{hoveredDoc.title}</p>
                </div>
              )
              :
              (
                <div className="pokedex-text-box title">
                  <p className="pokedex-text-box-text title">{"Search Results"}</p>
                </div>
              )
            }
            {
              hoveredDoc? 
              (
                <div className="pokedex-text-box description">
                  <p className="pokedex-text-box-text">{hoveredDoc.plot}</p>
                </div>
              )
              :
              (
                <div className="pokedex-text-box description">
                  <p className="pokedex-text-box-text">{"Search results are listed in the box beside! You can filter them if you want."}</p>
                </div>
              )
            }
            <div className="pokedex-items-list-container">
               <ul className="pokedex-items-list">
               {  
                  docs.map((doc)=>{
                    return (
                      <li className="pokedex-items-list-item"  key={doc.id} onMouseEnter={() => handleMouseEnter(doc)}>
                          <Image props={itemLogoProps} classList={["pokedex-items-list-item-logo"]}/>
                          <div className="pokedex-items-list-item-id">{doc.id}</div>
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
