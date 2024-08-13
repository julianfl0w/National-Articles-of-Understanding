
const toggleButton = document.getElementById('toggle-dark-mode');
const bodyElement = document.body;

toggleButton.addEventListener('click', () => {
    if (bodyElement.classList.contains('dark-mode')) {
        bodyElement.classList.remove('dark-mode');
        bodyElement.classList.add('light-mode');
        toggleButton.textContent = 'Dark Mode';
    } else {
        bodyElement.classList.remove('light-mode');
        bodyElement.classList.add('dark-mode');
        toggleButton.textContent = 'Light Mode';
    }
});
