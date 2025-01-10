function addTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-desc').value;
    const tasksContainer = document.getElementById('tasks-container');

    if (title.trim() === '') {
        alert('Please enter a task title.');
        return;
    }

    const taskItem = document.createElement('div');
    taskItem.className = 'task-item';
    taskItem.innerHTML = `<strong>${title}</strong><p>${description}</p><button onclick="removeTask(this)">Remove</button>`;

    tasksContainer.appendChild(taskItem);
    clearForm();
}

function clearForm() {
    document.getElementById('task-title').value = '';
    document.getElementById('task-desc').value = '';
}

function removeTask(button) {
    const taskItem = button.parentElement;
    taskItem.remove();
}