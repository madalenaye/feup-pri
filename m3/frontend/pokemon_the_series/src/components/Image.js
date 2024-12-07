export default function Image({classList=[],props}){
    const classlist = [...classList];
    return(
        <img className={classlist.join(" ")} {...props}/>
    )
}