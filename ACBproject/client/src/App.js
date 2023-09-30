import React from 'react';
import './App.css';
import Members from './Members'; 
import Display from './Display'; 
import Home from './Home'; 
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/members' element={<Members />} />
            <Route path='/Display' element={<Display />} />
          </Routes>
        </header>
      </div>
    </Router>
  );
}

export default App;