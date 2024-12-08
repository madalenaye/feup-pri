export default function Video({src,ariaLabel,classList}){
    const classlist= [...classList]
    return(
      <video src={src} loop autoPlay muted width={visualViewport.width} height={visualViewport.height} className={classlist.join(" ")} aria-label={ariaLabel}></video>
    );
  }