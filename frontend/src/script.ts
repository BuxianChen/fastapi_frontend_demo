async function invokeAPI() {
    const inputText = (document.getElementById('inputText') as HTMLInputElement).value;
    const response = await fetch('/invoke', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({text: inputText})
    });
    const data = await response.json();
    const outputText = document.getElementById('outputText') as HTMLSpanElement;
    outputText.textContent = data.result;
}
