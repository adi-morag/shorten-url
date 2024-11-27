import axios from 'axios';

const request = axios.create({ baseURL: 'http://localhost:5000' });

const shortenURL = async (longURL = '') => {
  try {
    const { data } = await request.post('/api/shorten', { url: longURL });
    return data.short_url;
  } catch (e) {
    console.log(`shortenURL request failed: ${e.message}`);
    throw e;
  }
}

export { shortenURL }