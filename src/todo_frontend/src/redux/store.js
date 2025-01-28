import { configureStore } from "@reduxjs/toolkit";
import todosReducer from "./todoReducer";

const store = configureStore({
    reducer: {
        todosData: todosReducer,
    }
})

export default store;