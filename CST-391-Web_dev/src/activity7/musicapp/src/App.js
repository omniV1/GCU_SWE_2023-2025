import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import NavBar from './Components/NavBar/NavBar';
import SearchAlbum from './Pages/SearchAlbum';
import NewAlbum from './Pages/NewAlbum';
import OneAlbum from './Pages/OneAlbum';
import EditAlbum from './Pages/EditAlbum';

const App = () => {
  return (
    <BrowserRouter>
      <div>
        <NavBar />
        <Routes>
          <Route path="/" element={<SearchAlbum />} />
          <Route path="/new" element={<NewAlbum />} />
          <Route path="/edit/:albumId" element={<EditAlbum />} />
          <Route path="/album/:albumId" element={<OneAlbum />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;