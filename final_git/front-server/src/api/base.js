// api/base.js
import axios from "axios"

function apiInstance() {
  const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
      "Content-Type" : "application/json;charset=utf-8",
    },
  });

  return instance;
}

export { apiInstance }