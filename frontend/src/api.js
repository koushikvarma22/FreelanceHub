import axios from "axios";

let baseURL = import.meta.env.VITE_API_URL || "http://localhost:5000/api";
baseURL = baseURL.replace(/\/+$/, "");
if (!baseURL.endsWith("/api")) {
  baseURL += "/api";
}

const api = axios.create({ baseURL });

api.interceptors.request.use((c) => {
  const token = localStorage.getItem("token");
  if (token) {
    c.headers.Authorization = `Bearer ${token}`;
  }
  return c;
});

export default api;
