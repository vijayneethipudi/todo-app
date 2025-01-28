import { useDispatch, useSelector } from "react-redux";
import React, { useState, useEffect } from "react";
import TodoEditForm from "./todoForm";

import { fetchTodos, addTodo, updateTodo, deleteTodo } from "../redux/todoActions";


function Todos() {
    const dispatch = useDispatch()
    const todos = useSelector((state) => state.todosData)

    const [editingTodo, setEditingTodo] = useState(null);
    const [isConfirmDelete, setIsConfirmDelete] = useState(false);
    const [todoToDelete, setTodoToDelete] = useState(null);

    // fetchtodos
    useEffect(() => {
        dispatch(fetchTodos())
    }, [dispatch])

    // update todo
    const handleEdit = (todo) => {
        setEditingTodo(todo);
    }

    const handleDelete = (todo) => {
        setTodoToDelete(todo);
        setIsConfirmDelete(true);
    };

    const confirmDelete = () => {
        dispatch(deleteTodo(todoToDelete.id));
        setIsConfirmDelete(false);
    };

    const cancelDelete = () => {
        setIsConfirmDelete(false);
    };

    const closeEditForm = () => {
        setEditingTodo(null);
    };

    // add todo form
    const [newTodo, setNewTodo] = useState(
        {
            title: "",
            description: "",
            completed: false
        }
    )
    const openModal = () => {
        setIsModalOpen(true);
    }

    const closeModal = () => {
        setIsModalOpen(false)
    }
    const handleAddTodo = () => {
        dispatch(addTodo(newTodo))
        setNewTodo({ title: "", description: "", completed: false })
        closeModal()
    }
    const [isModelOpen, setIsModalOpen] = useState(false)


    return (
        <div className="main-content">
            <h3>Todo App</h3>
            <button className="add-new-todo" onClick={openModal}>Add New Todo</button>
            {isModelOpen && (
                <div className="modal">
                    <div className="modal-content">
                        <button className="close-btn" onClick={closeModal}>X</button>
                        <h2>Add New Todo</h2>
                        <form onSubmit={handleAddTodo}>
                            <div>
                                <label>Title:</label>
                                <input
                                    type="text"
                                    value={newTodo.title}
                                    onChange={(e) => setNewTodo({ ...newTodo, title: e.target.value })}
                                    placeholder="Enter Todo Title"
                                    required
                                />
                            </div>
                            <div>
                                <label>Description:</label>
                                <textarea
                                    value={newTodo.description}
                                    onChange={(e) => setNewTodo({ ...newTodo, description: e.target.value })}
                                    placeholder="Enter Todo Description"
                                    required
                                />
                            </div>
                            <div>
                                <label>Completed:</label>
                                <input
                                    type="checkbox"
                                    checked={newTodo.completed}
                                    onChange={(e) => setNewTodo({ ...newTodo, completed: e.target.checked })}
                                />
                            </div>
                            <button type="submit">Submit</button>
                        </form>
                    </div>
                </div>
            )}

            {/* Delete Todo */}
            {isConfirmDelete && (
                <div className="confirm-modal">
                    <div className="confirm-modal-content">
                        <p>Are you sure you want to delete this todo?</p>
                        <button onClick={confirmDelete}>Yes</button>
                        <button onClick={cancelDelete}>No</button>
                    </div>
                </div>
            )}

            {/* Todo Edit Form */}
            {editingTodo && (
                <TodoEditForm
                    todo={editingTodo}
                    closeForm={closeEditForm}
                    updateTodo={updateTodo}
                />
            )}

            <table className="todo-table">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Description</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {todos.todos.map(todo => (
                        <tr key={todo.id}>
                            <td>{todo.title}</td>
                            <td>{todo.description}</td>
                            <td>{todo.completed ? "Completed" : "Incomplete"}</td>
                            <td>
                                <button className="update-btn" onClick={() => handleEdit(todo)}>Edit</button>
                                <button className="delete-btn" onClick={() => handleDelete(todo)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}


export default Todos;