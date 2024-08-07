function startScan() {
    const url = document.getElementById('url').value;
    const output = document.getElementById('output');
    output.textContent = 'Scanning...';

    fetch('/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        output.textContent = data.result;
    })
    .catch(error => {
        output.textContent = 'Error: ' + error.message;
    });
}
