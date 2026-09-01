import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export async function postRegister(name: string) {
    const response = await axios.post(API_URL + "/user/", { name });
    return response.data;
}

export async function postLogin(username: string) {
    const response = await axios.post(API_URL + "/login/" + username + "/");
    return response.data;
}