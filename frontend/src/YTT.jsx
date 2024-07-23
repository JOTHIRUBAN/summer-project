import React, { useState } from 'react';
import axios from 'axios';
import './YTT.css';

const YTT = () => {
  const [youtubeLink, setYoutubeLink] = useState('');
  const [summary, setSummary] = useState('');
  const [videoId, setVideoId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const video_id = youtubeLink.split("=")[1];
    setVideoId(video_id);

    try {
    console.log(youtubeLink);
      const res = await axios.post('http://localhost:5000/summary', { youtubeLink });
      setSummary(res.data.summary);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="yt-container">
      <h1>YouTube Transcript to Detailed Notes Converter</h1>
      <form className="yt-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter YouTube Video Link"
          value={youtubeLink}
          onChange={(e) => setYoutubeLink(e.target.value)}
          className="yt-input"
        />
        <button type="submit" className="yt-submit-button">Get Detailed Notes</button>
      </form>
      {videoId && <img src={`http://img.youtube.com/vi/${videoId}/0.jpg`} alt="Video Thumbnail" className="yt-thumbnail" />}
      {summary && (
        <div className="yt-summary">
          <h2>Detailed Notes:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
};

export default YTT;
