export default function Image({classList=[],props}){
    const classlist = [...classList];
    return(
        <img referrerPolicy="no-referrer" className={classlist.join(" ")} {...props}/>
    )
}