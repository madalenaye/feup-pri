import pokedexSearchBar from '../images/pokedexSearchBar.png';
import Search from '../images/Search.png'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import {useState} from 'react';
import LoadingBall from './LoadingBall';
import Image from './Image'
import Pokeball from "../images/pokeball.png"
export default function SearchBar() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [isEpisode, setIsEpisode] = useState(false);
  function handleResponse(response){
    if(!response) {
      console.warn("No response given from the server")
      throw new Error("No response");
    };
    console.log()
    const responseData = response.data;
    const docs = responseData
    navigate('/searchresults', { state: { docs, isEpisode} });
  }

  async function onSubmitRequest(event){
    event.preventDefault();
    const formField = event.target.querySelector('.search-bar-text-field');
    const query = formField.value;
    sessionStorage.setItem("lastQuery", query);
    const requestEndpoint = isEpisode?'http://127.0.0.1:5001/queryEpisodes/':'http://127.0.0.1:5001/queryPokemons/'
    let response;
    try {
      setLoading(true);
      console.log("query: ",query)
      response = await axios.post(
        requestEndpoint,
        { "query":query },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally{
      setLoading(false);
      handleResponse(response);
    }
    
  }
  const switchClickHandler=()=>{    
    setIsEpisode(!isEpisode);
  }
  const pokeballprops={
    src:Pokeball,
    className: isEpisode?"search-bar-switch activated":"search-bar-switch",
    onClick:switchClickHandler
  }
  return (
    <form className="search-bar" onSubmit={onSubmitRequest}>
        <SearchBarIcon src={pokedexSearchBar} classList={["search-bar-icon"]}/>
        <div className="search-bar-input">
          <div className="search-bar-placeholder"/>
          <input type="text" className="search-bar-text-field" placeholder="Ask anything!" defaultValue={sessionStorage.getItem("lastQuery")} required/>
        </div>
        {
          loading
          ? 
          <LoadingBall classList={["search-loading"]} />
          :
          <button type="submit" className="search-bar-button" > <SearchIcon props={{src:Search, className:"select"}}/></button>
        }
        <div className='search-bar-switch-container'>
          <Image props={pokeballprops}/>
          <div className={isEpisode?"search-bar-switch-text activated":"search-bar-switch-text"}>{isEpisode?"EP":"Poké"}</div>
        </div>
    </form>
  );
}
function SearchBarIcon({src,classList=[]}){
    const classlist = [...classList]
    return(
      <img src={src} className={classlist.join(" ")} alt="search bar pokedex icon"/>
    );
}
function SearchIcon({props={}}){
  
    return(
      <img {...props} alt="search icon on the search bar"/>
    );
}