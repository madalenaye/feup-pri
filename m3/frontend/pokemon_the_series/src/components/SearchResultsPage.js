import { useLocation } from "react-router-dom";
export default function SearchResultsPage() {
  const location = useLocation();
  const { docs } = location.state;
  return (
    <div>
      {docs.map((doc) =>{
        return (
          <div key={doc.id}>
            <h2>{doc.id}</h2>
            <p>{doc.title}</p>
            <p>{doc.plot}</p>
          </div>
        );
      })}
    </div>
  );
}
