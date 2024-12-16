import Pokeball from "../images/pokeball.png"
import Image from "./Image";
export default function Filters({props={},callbacks={},isEpisode=false}){

    const onChangeHandler= (event)=>{
        const orderType = event.target.value;
        const filterHandler = callbacks.filterHandler;
        filterHandler(orderType);
    }
    const onChangeLimitHandler = (event)=>{
        const limitNumber  =event.target.value;
        const limitHandler = callbacks.limitHandler;
        limitHandler(limitNumber);
    }
    const onChangeTypeHandler = (event)=>{
        const type = event.target.value;
        const typeHandler = callbacks.typeHandler;
        typeHandler(type);
    }

    const switchClickHandler=()=>{    
        const switchHandler = callbacks.switchHandler;
        switchHandler();
      }
      const switchprops={
        className: props.japaneseDate?"filter-switch":"filter-switch activated",
        onClick:switchClickHandler
      }
   
    const onDateSubmit=(event)=>{
        const button = event.target;
        const sw = button.previousElementSibling;
        const dateEndField = sw.previousElementSibling;
        const dateBeginField = dateEndField.previousElementSibling;

        const setDateHandler = callbacks.setDateHandler;
        setDateHandler(dateBeginField.value,dateEndField.value);
        
    }

    
    return(
        <div className="filters">
            Order By: 
            
            <select name="orderBy" className={props.className} onChange={onChangeHandler} >
                <option value="relevance" defaultValue="revelance">Relevance</option>
                <option value="idASc">Code Asc</option>
                <option value="idDesc">Code Desc</option>
                <option value="nameAsc">Name Asc</option>
                <option value="nameDesc">Name Desc</option>

            </select>
            
            Limit:
            
            <input type="number" className={props.className} defaultValue={30} step={30} min={0} onChange={onChangeLimitHandler}/>
            
            {isEpisode? "Date Begin: ":"Type: "}
            
            {   
                isEpisode?
                <input className={props.className} type="date" placeholder="Date"/>
                :
                <input className={props.className} placeholder="Type" onChange={onChangeTypeHandler}/>
            }
            
            {isEpisode? "Date End: ":null}
            
            {
                isEpisode?
                <input className={props.className} type="date" placeholder="Date"/>
                :null

            }
            {
                isEpisode?
                    <div className='filter-switch-container'>
                        <div {...switchprops}>{props.japaneseDate?"JP":"USA"}</div>
                    </div>
                :
                null
            }
            
            {isEpisode?<button onClick={onDateSubmit} className="filter-date-button">Filter Date</button>:null}
            
           
        </div>
    )
}