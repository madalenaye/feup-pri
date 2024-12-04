import pokeball from "../images/pokeball.png"
import johtoBadges from "../images/johto-badges.png"
import Video from "./Video.js"
import backGroundLoop from "../videos/backgroundLoop.mp4"
export default function MainMenu() {
    
    return (
      <div className="main-menu h-screen">
        <Video src={backGroundLoop} ariaLabel="Background video blue with a rotating pokeball bymbol" classList={["opacity-80", "-z-10" ,"absolute","video-background"]}/>
        <div className="top-bar">
            <h1>Header</h1>
        </div>
        <div className="main-menu-item1 flex-row flex-wrap content-center justify-items-center">
            <Pokeball src={pokeball} classList={["hover:bg-gray-100"]}/>
        </div>
        <div className="main-menu-item2  flex-row flex-wrap content-center justify-items-center">
            <Badges src={johtoBadges}/>
        </div>
        <footer className="footer">
            <h1>All rights reserved</h1>
        </footer>
      </div>
    );
}


function Pokeball({src,classList}){
    const classlist = [...classList]
    return(
        <img className={classlist.join(" ")} id="pokeball" src={src} alt="Pokeball logo"/>
    );
}
function Badges ({src}){
    return(
        <img className="" id="badge" src={src} alt="Johto Badges image"/>
    );
}
  