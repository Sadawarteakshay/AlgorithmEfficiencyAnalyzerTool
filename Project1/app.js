function generateRandomArray(size) {
    return Array.from({length: size}, () => Math.floor(Math.random() * 100));
}

function getSelectedAlgorithms() {
    const algorithms = document.querySelectorAll('input[name="algorithm"]:checked');
    return Array.from(algorithms).map(alg => alg.value);
}

function generateGraph() {
    const size = document.getElementById('arraySize').value;
    const manualInput = document.getElementById('manualArrayInput').value;
    const array = size ? generateRandomArray(size) : manualInput.split(' ').map(Number);
    const selectedAlgorithms = getSelectedAlgorithms();

    // Placeholder for runtime calculation logic
    console.log(array, selectedAlgorithms);

    // Placeholder for Chart.js graph generation
    // You will replace this with actual runtime data fetching and Chart.js usage
}

document.getElementById('runtimeChart').getContext('2d');
// Initialize Chart.js chart here based on your runtime data
