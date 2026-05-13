// API client for task management
const API_BASE_URL = '/api/tasks';

export const createTask = async (taskData) => {
    const response = await fetch(API_BASE_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData),
    });
    return response.json();
};

export const getTasks = async () => {
    const response = await fetch(API_BASE_URL);
    return response.json();
};

export const getTask = async (taskId) => {
    const response = await fetch(`${API_BASE_URL}/${taskId}`);
    return response.json();
};

export const updateTask = async (taskId, taskData) => {
    const response = await fetch(`${API_BASE_URL}/${taskId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(taskData),
    });
    return response.json();
};

export const deleteTask = async (taskId) => {
    const response = await fetch(`${API_BASE_URL}/${taskId}`, {
        method: 'DELETE',
    });
    return response.json();
};