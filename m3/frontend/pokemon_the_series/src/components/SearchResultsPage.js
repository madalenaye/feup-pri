export default function SearchResultsPage() {
  return (
    <form className="search-bar" onSubmit={(e)=>{e.preventDefault()}}>
        <div className="search-bar-input">
          <div className="search-bar-placeholder"/>
          <input type="text" className="search-bar-text-field" placeholder="Make your query here!" required/>
        </div>
        <button type="submit" className="search-bar-button" > <SearchIcon src={Search} classList={["select"]}/></button>
    </form>
  );
}
