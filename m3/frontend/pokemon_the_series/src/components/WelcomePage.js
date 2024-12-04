import "../css/App.css";
import { useEffect } from "react";
import backgroundLoop1 from "../videos/backgroundLoop1.mp4"
import logo from "../images/logo.png"
import { useState } from "react";
export default function WelcomePage() {
    	
    useEffect(() => {

    },[]);
    
    return (
      <div className="h-screen w-screen flex flex-wrap content-center justify-center z-50">
        <Video source={backgroundLoop1}/>
        <Logo source={logo}/>
          <div className=" flex-col content-end h-screen animate-pulse mb-12 -z-5">
            <h1>
              Press anywhere to continue
            </h1>
          </div>
      
      </div>
    );
  }

  function Video({source}){
    return(
      <video src={source} loop autoPlay muted width={visualViewport.width} height={visualViewport.height} className="opacity-100 -z-10 absolute w-full h-full"></video>
    );
  }
  function Logo({source}){
    return(
      <img src={source} className=" fixed w-4/12 logoAnimation"/>
    );
  }