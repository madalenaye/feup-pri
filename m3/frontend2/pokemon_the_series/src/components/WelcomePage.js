import "../css/App.css";
import { useEffect } from "react";
export default function WelcomePage() {
    useEffect(() => {
      const body = document.body;
      body.classList.add("bg-yellow-300");
      body.classList.add("h-full");
      body.classList.add("flex-col");
      body.classList.add("contents-center");
    },[]);
    return (
        <div>
        <h1>Welcome to Ash's Archive</h1>
        <button>Get started</button>
      </div>
    );
  }
  
  