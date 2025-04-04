function clickButton() {
    fetch(`/api/increment`, { method: 'POST' }) // Use backticks for template literals
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('click-count').textContent = data.count; // Update the count displayed on the page
        })
        .catch(error => console.error('Error:', error)); // Handle errors
}