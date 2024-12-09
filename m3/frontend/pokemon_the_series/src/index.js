import React from 'react';
import ReactDOM from 'react-dom/client';
import './css/index.css';
import 'tailwindcss/tailwind.css';
import './components/WelcomePage.js';
import reportWebVitals from './reportWebVitals';
import Navigator from './components/Navigator.js'
import { BrowserRouter } from 'react-router-dom';
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Navigator/>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
