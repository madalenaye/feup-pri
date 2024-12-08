import pokedexSearchBar from '../images/pokedexSearchBar.png';
import Search from '../images/Search.png'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import {useState} from 'react';
import LoadingBall from './LoadingBall';
export default function SearchBar() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  function handleResponse(response){
    const responseData = response.data;
    const docs = responseData.response.docs
    navigate('/searchresults', { state: { docs } });
  }

  async function onSubmitRequest(event){
    event.preventDefault();
    const formField = event.target.querySelector('.search-bar-text-field');
    const query = formField.value;
    let response;
    try {
      setLoading(true);
      response = await axios.post(
        'http://127.0.0.1:5001/query/',
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
  return (
    <form className="search-bar" onSubmit={onSubmitRequest}>
        <SearchBarIcon src={pokedexSearchBar} classList={["search-bar-icon"]}/>
        <div className="search-bar-input">
          <div className="search-bar-placeholder"/>
          <input type="text" className="search-bar-text-field" placeholder="Make your query here!" required/>
        </div>
        {
          loading
          ? 
          <LoadingBall classList={["search-loading"]} />
          :
          <button type="submit" className="search-bar-button" > <SearchIcon src={Search} classList={["select"]}/></button>
        }
    </form>
  );
}
function SearchBarIcon({src,classList=[]}){
    const classlist = [...classList]
    return(
      <img src={src} className={classlist.join(" ")} alt="search bar pokedex icon"/>
    );
}
function SearchIcon({src,classList=[]}){
  const classlist = [...classList]
    return(
      <img src={src} className={classlist.join(" ")} alt="search icon on the search bar"/>
    );
}