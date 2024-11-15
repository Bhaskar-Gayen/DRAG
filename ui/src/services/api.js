import axios from "axios";

const API_URL = "http://localhost:8000/api";

export const login = (username, password) => {
  return axios.post(`${API_URL}/auth/login`, { username, password });
};

export const register = (username, email, password) => {
  return axios.post(`${API_URL}/auth/register`, { username, email, password });
};
