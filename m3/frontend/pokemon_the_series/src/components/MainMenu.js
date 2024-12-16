import badge from "../images/badge.webp"
import Video from "./Video.js"
import logo from "../images/logo.png"
import Image from "./Image.js"
import backGroundLoop from "../videos/backgroundLoop.mp4"
import SearchBar from "./SearchBar.js"
import Tips from "./Tips.js"

export default function MainMenu() {
    
    const badgeProps = {
        src:badge,
        id:"header-logo",
        alt:"Badge logo"
    }
    const searchEngineLogoProps={
        src:logo,
        id:"search-engine-name",
        alt:"Name of the website"
    }
    return (
      <div className="main-menu h-screen">
        <Video src={backGroundLoop} ariaLabel="Background video blue with a rotating pokeball bymbol" classList={["opacity-80", "-z-10" ,"absolute","video-background"]}/>
        <div className="top-bar">
            <Image props={badgeProps} classList={["select","topbar-icon"]}/>
        </div>
        
        <div className="main-menu-content search-engine-container">
            <Image props={searchEngineLogoProps} classList={["select","above-search-tab"]}/>
            <SearchBar/>
            <Tips classList={["search-engine-tips"]}/>
        </div>
        <footer className="footer">
            <h1>All rights reserved</h1>
        </footer>
      </div>
    );
}
