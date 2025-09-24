import React, { useState } from 'react';
import Post from './Post';
import AddPost from './AddPost';

const App = () => {
  const [postList, setPostList] = useState([
    { id: 3, text: "Third blog post. I have run out of ideas. Please comment below." },
    { id: 2, text: "More interesting reading if only I had more time..." },
    { id: 1, text: "A very interesting blog post about nothing." }
  ]);
  const [postId, setPostId] = useState(4);

  const handleAddPost = (postText) => {
    const newPost = {
      id: postId,
      text: postText
    };
    // Add new post to the beginning of the list
    setPostList(currentPosts => [newPost, ...currentPosts]);
    setPostId(postId + 1);
  };

  const handleDeletePost = (id) => {
    const updatedPostList = postList.filter(post => post.id !== id);
    setPostList(updatedPostList);
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <AddPost onAddPost={handleAddPost} />
      <div>
        {postList.map(post => (
          <Post 
            key={post.id}
            id={post.id}
            text={post.text}
            onDelete={handleDeletePost}
          />
        ))}
      </div>
    </div>
  );
};

export default App;