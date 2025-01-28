import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { updateTodo } from '../redux/todoActions';

const TodoEditForm = ({ todo, closeForm }) => {
    const dispatch = useDispatch();

    const [title, setTitle] = useState(todo.title);
    const [description, setDescription] = useState(todo.description);
    const [completed, setCompleted] = useState(todo.completed);

    const handleSubmit = (e) => {
        e.preventDefault();

        const updatedTodo = {
            ...todo,
            title,
            description,
            completed,
        };

        dispatch(updateTodo(todo.id, updatedTodo));
        closeForm();
    };

    return (
        <div className="modal">
            <div className="modal-content">
                <button className="close-btn" onClick={closeForm}>X</button>
                <h2>Edit Todo</h2>
                <form onSubmit={handleSubmit}>
                    <div>
                        <label>Title:</label>
                        <input
                            type="text"
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label>Description:</label>
                        <textarea
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                            required
                        />
                    </div>
                    <div>
                        <label>Completed:</label>
                        <input
                            type="checkbox"
                            checked={completed}
                            onChange={(e) => setCompleted(e.target.checked)}
                        />
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </div>
    );
};

export default TodoEditForm;