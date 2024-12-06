import pokedexSearchBar from '../images/pokedexSearchBar.png';
import Search from '../images/Search.png'
export default function SearchBar() {
  return (
    <form className="search-bar" onSubmit={(e)=>{e.preventDefault()}}>
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