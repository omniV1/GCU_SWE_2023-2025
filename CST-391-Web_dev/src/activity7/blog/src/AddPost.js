import React, { useState } from 'react';

const AddPost = ({ onAddPost }) => {
  const [postText, setPostText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (postText.trim()) {
      onAddPost(postText);
      setPostText('');
    }
  };

  return (
    <div className="add-post">
      <form onSubmit={handleSubmit}>
        <textarea
          value={postText}
          onChange={(e) => setPostText(e.target.value)}
          placeholder="Enter your blog post..."
          rows="3"
        />
        <div>
          <button type="submit">Add</button>
        </div>
      </form>
    </div>
  );
};

export default AddPost;