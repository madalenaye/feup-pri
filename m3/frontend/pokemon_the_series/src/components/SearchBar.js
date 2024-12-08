import pokedexSearchBar from '../images/pokedexSearchBar.png';
import Search from '../images/Search.png'
import axios from 'axios';

export default function SearchBar() {

  async function onSubmitRequest(event){
    event.preventDefault();
    const formField = event.target.querySelector('.search-bar-text-field');
    const query = formField.value;
    try {
      const response = await axios.post(
        'http://127.0.0.1:5002/query/',
        { "query":query },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      console.log('Data fetched:', response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }
  return (
    <form className="search-bar" onSubmit={onSubmitRequest}>
      
        <SearchBarIcon src={pokedexSearchBar} classList={["search-bar-icon"]}/>
        <div className="search-bar-input">
          <div className="search-bar-placeholder"/>
          <input type="text" className="search-bar-text-field" placeholder="Make your query here!" required/>
        </div>
        <button type="submit" className="search-bar-button" > <SearchIcon src={Search} classList={["select"]}/></button>
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