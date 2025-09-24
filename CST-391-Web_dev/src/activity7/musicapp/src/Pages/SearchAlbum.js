import React, { useState, useEffect } from 'react';
import SearchForm from '../Components/SearchForm/SearchForm';
import Card from '../Components/Card/Card';
import dataSource from '../Services/dataSource';

const SearchAlbum = () => {
  const [albumList, setAlbumList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadAlbums();
  }, []);

  const loadAlbums = async () => {
    try {
      setLoading(true);
      const albums = await dataSource.getAllAlbums();
      console.log('Loaded albums:', albums); // Debug log
      setAlbumList(albums);
      setError(null);
    } catch (err) {
      console.error("Failed to load albums:", err);
      setError("Failed to load albums. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (searchText) => {
    try {
      setLoading(true);
      if (searchText.trim()) {
        const results = await dataSource.searchAlbums(searchText);
        setAlbumList(results);
      } else {
        await loadAlbums();
      }
      setError(null);
    } catch (err) {
      console.error("Search failed:", err);
      setError("Failed to search albums. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const renderContent = () => {
    if (loading) {
      return (
        <div className="col-12 text-center">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      );
    }

    if (error) {
      return (
        <div className="col-12">
          <div className="alert alert-danger" role="alert">
            {error}
          </div>
        </div>
      );
    }

    if (albumList.length === 0) {
      return (
        <div className="col-12">
          <div className="alert alert-info" role="alert">
            No albums found. Try a different search term.
          </div>
        </div>
      );
    }

    return albumList.map((album) => (
      <Card key={album.id} album={album} /> // Pass the entire album object
    ));
  };

  return (
    <div className="container py-4">
      <SearchForm onSubmit={handleSearch} />
      <div className="row">
        {renderContent()}
      </div>
    </div>
  );
};

export default SearchAlbum;