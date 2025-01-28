import axios from "axios"

// Action types
export const FETCH_TODOS = "FETCH_TODOS"
export const ADD_TODO = "ADD_TODO"
export const DELETE_TODO = "DELETE_TODO"
export const UPDATE_TODO = "UPDATE_TODO"


const REACT_APP_BASE_URL = "http://localhost:8000"
const ENDPOINT = "/todos"

export const fetchTodos = () => async (dispatch) => {
    try {
        const response = await axios.get(`${REACT_APP_BASE_URL}${ENDPOINT}`)
        dispatch({
            type: FETCH_TODOS,
            payload: response.data
        });
    } catch (error) {
        console.error("Unable to fetch todos", error)
    }
}

export const addTodo = (todo) => async (dispatch) => {
    try {
        const response = await axios.post(`${REACT_APP_BASE_URL}${ENDPOINT}`, todo)
        dispatch({
            type: ADD_TODO,
            payload: response.data
        })
    } catch (error) {
        console.error("Unable to Add todo", error)
    }
}

export const updateTodo = (id, updateTodo) => async (dispatch) => {
    try {
        const response = await axios.put(`${REACT_APP_BASE_URL}${ENDPOINT}/${id}`, updateTodo)
        dispatch({
            type: UPDATE_TODO,
            payload: response.data
        })
    } catch (error) {
        console.error("Unable to update todo", error)
    }
}

export const deleteTodo = (id) => async (dispatch) => {
    try {
        await axios.delete(`${REACT_APP_BASE_URL}${ENDPOINT}/${id}`)
        dispatch({
            type: DELETE_TODO,
            payload: id
        })
    } catch (error) {
        console.error("Unable to delete todo", error)
    }
}