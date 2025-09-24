import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import NavBar from './Components/NavBar/NavBar.js';
import SearchAlbum from './Pages/SearchAlbum.js';
import NewAlbum from './Pages/NewAlbum.js';
import OneAlbum from './Pages/OneAlbum.js';
import './Styles/App.css';

const App = () => {
  const [currentlySelectedAlbumId, setCurrentlySelectedAlbumId] = useState(null);

  const updateSingleAlbum = (id) => {
    setCurrentlySelectedAlbumId(id);
  };

  return (
    <BrowserRouter>
      <div>
        <NavBar />
        <Routes>
          <Route 
            path="/" 
            element={<SearchAlbum onAlbumSelect={updateSingleAlbum} />} 
          />
          <Route 
            path="/new" 
            element={<NewAlbum />} 
          />
          <Route 
            path="/show/:albumId" 
            element={<OneAlbum albumId={currentlySelectedAlbumId} />} 
          />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;