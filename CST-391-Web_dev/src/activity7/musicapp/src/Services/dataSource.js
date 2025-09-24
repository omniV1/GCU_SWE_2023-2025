import axios from 'axios';

const baseUrl = "http://localhost:3001/api"; // Added /api to match server routes

/**
 * DataSource class provides methods to interact with the music albums API.
 */
class DataSource {
  /**
   * Fetches all albums from the API.
   * @returns {Promise<Array>} A promise that resolves to an array of album objects.
   * @throws Will throw an error if the request fails.
   */
  async getAllAlbums() {}

  /**
   * Searches for albums based on a search term.
   * @param {string} searchTerm - The term to search for.
   * @returns {Promise<Array>} A promise that resolves to an array of album objects matching the search term.
   * @throws Will throw an error if the request fails.
   */
  async searchAlbums(searchTerm) {}

  /**
   * Creates a new album.
   * @param {Object} albumData - The data of the album to create.
   * @returns {Promise<Object>} A promise that resolves to the created album object.
   * @throws Will throw an error if the request fails.
   */
  async createAlbum(albumData) {}

  /**
   * Fetches an album by its ID.
   * @param {number|string} id - The ID of the album to fetch.
   * @returns {Promise<Object>} A promise that resolves to the album object.
   * @throws Will throw an error if the request fails.
   */
  async getAlbumById(id) {}

  /**
   * Fetches the tracks of a specific album.
   * @param {number|string} albumId - The ID of the album whose tracks are to be fetched.
   * @returns {Promise<Array>} A promise that resolves to an array of track objects.
   * @throws Will throw an error if the request fails.
   */
  async getAlbumTracks(albumId) {
    try {
      const response = await axios.get(`${baseUrl}/albums/${albumId}/tracks`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching tracks for album ${albumId}:`, error);
      throw error;
    }
  }
}

const dataSourceInstance = new DataSource();
export default dataSourceInstance;