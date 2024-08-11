import React from 'react';
import Desktop from './pages/Desktop';
import '@fortawesome/fontawesome-free/css/all.min.css';
import Logo from './components/Logo';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import SignUp from './components/SignUp';

const App = () => {
  return (
    <div>
      
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Desktop />} />
          <Route path="/login" element={<Login />} />
          <Route path="/create-account" element={<SignUp />} />
        </Routes>
      </BrowserRouter>
      
    </div>
  );
};

export default App;
