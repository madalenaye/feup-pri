export default function Filters({props={},callbacks={}}){
    const onChangeHandler= (event)=>{
        const orderType = event.target.value;
        const filterHandler = callbacks.filterHandler;
        filterHandler(orderType);
    }
    const onChangeLimitHandler = (event)=>{
        const limitNumber  =event.target.value;
        console.log("target value:",limitNumber)
        const limitHandler = callbacks.limitHandler;
        limitHandler(limitNumber);
    }
    return(
        <div>
            Order By: 
            &nbsp;
            <select name="orderBy" {...props} onChange={onChangeHandler} >
                <option value="relevance" defaultValue="revelance">Relevance</option>
                <option value="id">Code</option>
                <option value="name">Name</option>
            </select>
            &nbsp;
            Limit:
            &nbsp;
            <input type="number" {...props} defaultValue={30} step={30} min={0} onChange={onChangeLimitHandler}/>
        </div>
    )
}