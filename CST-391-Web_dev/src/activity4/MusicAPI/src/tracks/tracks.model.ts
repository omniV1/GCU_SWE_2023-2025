/**
 * Defines the structure of a Track entity.
 */
export interface Track {
    trackId: number; // Unique identifier for the track
    title: string; // Title of the track
    number: number; // Track number in the album
    video: string; // URL or path to the video of the track
    lyrics: string; // Lyrics of the track
}
