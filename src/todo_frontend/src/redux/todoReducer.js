import { FETCH_TODOS, ADD_TODO, UPDATE_TODO, DELETE_TODO } from "./todoActions";

const initialState = {
    todos: []
}

const todosReducer = (state = initialState, action) => {
    switch (action.type) {
        case FETCH_TODOS:
            return {
                ...state,
                todos: action.payload
            }
        case ADD_TODO:
            return {
                ...state,
                todos: [...state.todos, action.payload]
            }
        case UPDATE_TODO:
            return {
                ...state,
                todos: state.todos.map((todo) => (todo.id === action.payload.id ? action.payload : todo))
            }
        case DELETE_TODO:
            return {
                ...state,
                todos: state.todos.filter((todo) => todo.id !== action.payload)
            }
        default:
            return state
    }
}

export default todosReducer;