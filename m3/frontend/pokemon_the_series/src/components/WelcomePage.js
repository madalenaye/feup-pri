import "../css/App.css";
import { useEffect } from "react";
import backgroundLoop1 from "../videos/backgroundLoop1.mp4"
import logo from "../images/logo.png"
import Video from "./Video.js"
import { useNavigate } from "react-router-dom";
export default function WelcomePage() {
    const navigate = useNavigate()
    useEffect(() => {

    },[]);
    function clickHandler(event){
      const clicked = event.target;
      const pressText = clicked.querySelector("#PressAnywhereToContinue")
      pressText.classList.add("animate-ping")
      setTimeout(()=>{
        navigate("/MainMenu")
      },900)
    }
    
    return (
      <div className="h-screen w-screen flex flex-wrap content-center justify-center z-50" onClick={clickHandler}>
        <Video src={backgroundLoop1} ariaLabel="Background video with Ash and his pokemons" classList={["opacity-100", "-z-10" ,"absolute", "w-full", "h-full"]} />
        <Logo source={logo}/>
        <div className="pulse absolute-bottom -z-5">
          <h1 className="text-3xl" id="PressAnywhereToContinue">
            Press anywhere to continue
          </h1>
        </div>
      </div>
    );
  }

  function Logo({source}){
    return(
      <img src={source} className=" fixed w-4/12 logoAnimation" alt="Ash's Archive"/>
    );
  }