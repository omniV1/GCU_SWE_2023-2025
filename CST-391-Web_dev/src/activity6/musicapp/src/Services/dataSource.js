import axios from 'axios';

// Base URL for your Express backend
const baseUrl = "http://localhost:3001"; // Make sure this matches your Express server port

class DataSource {
  async getAllAlbums() {
    try {
      const response = await axios.get(`${baseUrl}/api/albums`);
      console.log("Albums fetched successfully:", response.data);
      return response.data;
    } catch (error) {
      console.error("Error fetching albums:", error);
      throw error;
    }
  }

  async searchAlbums(searchTerm) {
    try {
      const response = await axios.get(`${baseUrl}/api/albums/search?term=${searchTerm}`);
      return response.data;
    } catch (error) {
      console.error("Error searching albums:", error);
      throw error;
    }
  }

  async getAlbumById(id) {
    try {
      const response = await axios.get(`${baseUrl}/api/albums/${id}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching album ${id}:`, error);
      throw error;
    }
  }
}

export default new DataSource();