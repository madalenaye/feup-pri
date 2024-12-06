import pokedex from "../images/pokedex.png"
import johtoBadges from "../images/johto-badges.png"
import badge from "../images/badge.webp"
import Video from "./Video.js"
import backGroundLoop from "../videos/backgroundLoop.mp4"
import SearchBar from "./SearchBar.js"
import Tips from "./Tips.js"

export default function MainMenu() {
    
    //not used yet
    /*const icons = (
        <div>
            <div className="main-menu-item1 flex-row flex-wrap content-center justify-items-center">
                <Pokedex src={pokedex}  classList={["select"]}/>
            </div>
            
            <div className="main-menu-item2  flex-row flex-wrap content-center justify-items-center">
                <Badges src={johtoBadges} classList={["select"]}/>
            </div>
        </div>
    );*/
    return (
      <div className="main-menu h-screen">
        <Video src={backGroundLoop} ariaLabel="Background video blue with a rotating pokeball bymbol" classList={["opacity-80", "-z-10" ,"absolute","video-background"]}/>
        <div className="top-bar flex-row content-center justify-items-end">
            <HeaderLogo src={badge} classList={["select"]}/>
        </div>
        <div className="main-menu-content search-engine-container">
            <SearchBar/>
            <Tips classList={["search-engine-tips"]}/>
        </div>
        <footer className="footer">
            <h1>All rights reserved</h1>
        </footer>
      </div>
    );
}

function HeaderLogo({src,classList=[]}){
    const classlist = [...classList];
    return(
        <img className={classlist.join(" ")} id="header-logo" src={src} alt="Badge logo"/>
    )
}
function Pokedex({src,classList=[]}){
    const classlist = [...classList]
    return(
        <img className={classlist.join(" ")} id="pokedex" src={src} alt="Pokeball logo"/>
    );
}
function Badges ({src,classList=[]}){
    const classlist = [...classList]
    
    return(
        <img className={classlist.join(" ")} id="badge" src={src} alt="Johto Badges image"/>
    );
}
