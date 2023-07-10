import React, { useState, useEffect } from 'react';

function Livestreams() {
  const [livestreams, setLivestreams] = useState([]);
  const [comment, setComment] = useState('');
  const [userId, setUserId] = useState(null); 


  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/livestreams/')
      .then((response) => response.json())
      .then((data) => {
        setLivestreams(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

//   const joinLivestream = (livestreamId) => {
//     fetch(`http://127.0.0.1:8000/api/livestreams/${livestreamId}/join/`, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         console.log(data);
//       })
//       .catch((error) => {
//         console.error('Error:', error);
//       });
//   };
    const joinLivestream = (livestreamId) => {
        fetch(`http://127.0.0.1:8000/api/livestreams/${livestreamId}/join/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            // user_id: userId, // Pass the user ID to the join endpoint 
            user_id: 2, // Pass the user ID to the join endpoint
        }),
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    };


  const leaveLivestream = (livestreamId) => {
    fetch(`http://127.0.0.1:8000/api/livestreams/${livestreamId}/leave/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const postComment = (livestreamId, comment) => {
    fetch(`http://127.0.0.1:8000/api/livestreams/${livestreamId}/comments/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        content: comment,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      {livestreams.map((livestream) => (
        <div key={livestream.id}>
          <h3>{livestream.title}</h3>
          <p>{livestream.description}</p>
          <p>Status: {livestream.status}</p>
          <button onClick={() => joinLivestream(livestream.id)}>Join</button>
          <button onClick={() => leaveLivestream(livestream.id)}>Leave</button>
          <input
            type="text"
            placeholder="Comment"
            onChange={(e) => setComment(e.target.value)}
          />
          <button onClick={() => postComment(livestream.id, comment)}>Post Comment</button>
        </div>
      ))}
    </div>
  );
}

export default Livestreams;
