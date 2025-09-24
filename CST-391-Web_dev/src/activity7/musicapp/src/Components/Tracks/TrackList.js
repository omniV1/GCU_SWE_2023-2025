import React from 'react';

const TrackList = ({ tracks, onTrackSelect, selectedTrack }) => {
  return (
    <div className="list-group">
      {tracks.map((track) => (
        <button
          key={track.id}
          className={`list-group-item list-group-item-action ${selectedTrack?.id === track.id ? 'active' : ''}`}
          onClick={() => onTrackSelect(track)}
        >
          {track.number}. {track.title}
        </button>
      ))}
    </div>
  );
};

export default TrackList;