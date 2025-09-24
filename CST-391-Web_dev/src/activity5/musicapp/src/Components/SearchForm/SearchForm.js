import React, { useState } from 'react';

const SearchForm = ({ onSubmit }) => {
  const [inputText, setInputText] = useState("");
  
  const handleChangeInput = (event) => {
    setInputText(event.target.value);
    console.log(`Search input changed to: ${event.target.value}`);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Search submitted with value: ${inputText}`);
    onSubmit(inputText);
  };

  return (
    <div className="container mb-4">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input 
            type="text" 
            className="form-control"
            placeholder="Search for albums..."
            aria-label="Search for albums"
            value={inputText}
            onChange={handleChangeInput}
          />
          <button 
            className="btn btn-primary" 
            type="submit"
          >
            Search
          </button>
        </div>
      </form>
    </div>
  );
};

export default SearchForm;