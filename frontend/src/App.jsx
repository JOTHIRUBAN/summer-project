import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Login from './Login';
import Signup from './Signup';
import ATS from './ATS';
import YTT from './YTT';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <Link className="nav-link" to="/login">Login</Link>
          <Link className="nav-link" to="/signup">Signup</Link>
          <Link className="nav-link" to="/ats">ATS</Link>
          <Link className="nav-link" to="/ytt">YTT</Link>
        </nav>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/ats" element={<ATS />} />
          <Route path="/ytt" element={<YTT />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
