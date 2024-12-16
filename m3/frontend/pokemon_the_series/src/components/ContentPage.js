import { useLocation, useNavigate } from "react-router-dom";
import Video from "./Video.js"
import Image from "./Image.js"
import badge from "../images/badge.webp"
import backGroundLoop from "../videos/backgroundLoop.mp4"
import Japan from "../images/japan.png";
import USA from "../images/usa.png";
import Pokeball from "../images/pokeball.png"
import Egg from "../images/egg.webp";
import Arrow from "../images/arrow.png"

import axios from "axios"
import { useState } from "react";
export default function ContentPage(){
    const location = useLocation();
    const navigate = useNavigate();
    const { doc,isEpisode } = location.state;
    const badgeClickHandler =()=>{
        navigate("/mainmenu");
    }
    const handleResponse = (response) =>{
        let docs = [...response.data]
        navigate("/searchresults",{state:{docs,isEpisode}})
    }
    async function morelikethisHandler(event){
        event.preventDefault();
        console.log("clicked!");
        const requestEndpoint = 'http://127.0.0.1:5001/morelikethis/'
        console.log(requestEndpoint)
        let response;
        try {
            response = await axios.post(
                requestEndpoint,
                {"id":doc.id},
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            );
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally{
            handleResponse(response)
        }
    }
    const badgeProps = {
            src:badge,
            id:"header-logo",
            alt:"Badge logo",
            onClick:badgeClickHandler,
    }
    
    const imageProps={
        src:doc.image,
        className:"page-image",
        alt:"Image of a pokemon or badge"
    }
    const convertToClassName = (type)=>{
       return type.toLowerCase();
    }
    let key=0;
    const genKey=()=>{
        key++;
        return key;
    }
    return(
        <div className="main-menu h-screen">
                <Video src={backGroundLoop} ariaLabel="Background video blue with a rotating pokeball bymbol" classList={["opacity-80", "-z-10" ,"absolute","video-background"]}/>
                <div className="top-bar">
                    <Image props={badgeProps} classList={["select","topbar-icon"]}/>
                </div>
                <div className="main-menu-content content-page">
                    <div className="content-page-entry">
                    <div className="content-page-image-container">
                                <h2 className="page-title">
                                <Image props={{src:Pokeball,alt:"pokeball icon",className:"page-title-logo"}} />
                                <div>{isEpisode?doc.id:doc.pokedex_entry}</div>
                                <div>{isEpisode?doc.title:doc.name}</div>
                                 </h2>
                            <Image props={imageProps}/>
                        </div>
                        <div className="content-page-short-info-container">
                              
                            <div className="short-info-box-skewed">
                                
                                <div className="short-info-box-content-col">
                                    <div className="short-info-box-content-row">
                                        <h3 className="short-info-box-content-title">{isEpisode?"First Broadcast":"Type/s"}</h3>
                                    </div>
                                    {
                                        isEpisode?
                                        <ul className="short-info-box-content-row">
                                            <li className={"tags fire"} key={"broadcastdatejapan"}>
                                                <Image props ={{src:Japan,alt:"Japanese flag",className:"flags"}}/>
                                                {doc.first_broadcast_japan.substring(0,10)}
                                            </li>
                                            <li className="tags fighting" key={"broadcastdateusa"}>
                                                <Image props ={{src:USA,alt:"USA flag",className:"flags"}}/>
                                                {doc.first_broadcast_united_states.substring(0,10)}
                                            </li>
                                        </ul>
                                        :
                                        <ul className="short-info-box-content-row">
                                            {   
                                                doc.types.map((type)=>{
                                                    if(type)
                                                        return(<li className={"tags "+ convertToClassName(type)}  key={type}>{type}</li>)
                                                    return null;
                                                })
                                            }

                                        </ul>
                                    }
                                    <div className="short-info-box-content-row">
                                        <h3 className="short-info-box-content-title">{isEpisode?"Themes":"Abilities"}</h3>
                                    </div>
                                    {
                                         isEpisode?
                                         <ul className="short-info-box-content-row">
                                            {
                                                doc.japanese_theme_opening?
                                                <li className={"tags fire"} key={"japanesethemeop"}>
                                                    <Image props ={{src:Japan,alt:"Japanese flag",className:"flags"}}/>
                                                    {doc.japanese_theme_opening}
                                                </li>
                                                :null
                                            }
                                            
                                            {
                                                doc.japanese_theme_opening?
                                                <li className="tags fighting" key={"usathemeop"}>
                                                    <Image props ={{src:USA,alt:"USA flag",className:"flags"}}/>
                                                    {doc.english_theme_opening}
                                                </li>
                                                :null
                                            }
                                            {
                                                doc.japanese_theme_ending?
                                                <li className={"tags fire"} key={"japanesethemeclose"}>
                                                    <Image props ={{src:Japan,alt:"Japanese flag",className:"flags"}}/>
                                                    {doc.japanese_theme_ending}
                                                </li>
                                                :null
                                            }
                                           
                                            {
                                                doc.english_theme_ending?
                                                <li className={"tags fighting"} key={"englishthemeclose"}>
                                                    <Image props ={{src:USA,alt:"USA flag",className:"flags"}}/>
                                                    {doc.english_theme_ending}
                                                </li>
                                                :null
                                            }
                                        </ul>
                                         :
                                         <ul className="short-info-box-content-row">
                                            {
                                                doc.abilities.map((ability)=>{
                                                    return <li className={"tags "+ convertToClassName(doc.types[0])} key={ability}>{ability}</li>
                                                })
                                            }
                                         </ul>
                                    }
                                    
                                    {
                                        isEpisode?
                                        <div className="short-info-box-content-row">
                                            <h3 className="short-info-box-content-title">{isEpisode?"Credits":null}</h3>
                                        </div>
                                        :null
                                    }
                                    {
                                        isEpisode?
                                            <ul className="short-info-box-content-row">
                                                {doc.animation?<li className="tags" key={genKey()}>{ "Animation: " + doc.animation}</li>:null}
                                                {doc.screenplay?<li className="tags" key={genKey()}>{"Screenplay: "+doc.screenplay}</li>:null}
                                                {doc.storyboard?<li className="tags" key={genKey()}>{"Storyboard: "+doc.storyboard}</li>:null}
                                                {doc.assistant_director?<li className="tags" key={genKey()}>{"Assistant Director: "+doc.assistant_director}</li>:null}
                                            </ul>
                                        :
                                        <></>
                                    }
                                </div>
                            </div>
                        </div>
                        <div className="content-page-long-info-container">
                            <div className="long-info-box-skewed">
                                <h2 className="long-info-box-title">{isEpisode?"Plot":"Biology"}</h2>
                                <div className="long-info-box-unskewed">
                                    {
                                        isEpisode?
                                        doc.paragraphs.map((paragraph)=>{
                                            return <p key={genKey()}>{paragraph}</p>
                                        })
                                        :
                                        <p>
                                            {doc.biology}
                                        </p>
                                    }
                                </div>
                            </div>
                        </div>
                        {
                            isEpisode?
                            <button onClick={morelikethisHandler} className="more-like-this-button">
                                More like this
                                <Image props={{src:Arrow,alt:"An arrow",className:"arrow"}}/>
                            </button>
                            :
                            null
                        }
                        <Image props={{src:Egg,alt:"An egg",className:"easter-egg"}}/>
                    </div>
                    
                </div>
                <footer className="footer">
                    <h1>All rights reserved</h1>
                </footer>
        </div>
    )

}