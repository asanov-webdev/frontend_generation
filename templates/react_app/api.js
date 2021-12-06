import axios from "./axios-config";

export async function fetchSomeData() {
  const data = await axios.get("/someUrl").then((response) => response.data);

  return data;
}

