let pieChart;


function showTextarea() {
    document.getElementById('articleForm').style.display = 'block';
    document.getElementById('urlForm').style.display = 'none';
    document.getElementById('fileForm').style.display = 'none';
    document.getElementById('articleText').style.marginBottom = '20px'; 
}


function showUrlInput() {
    document.getElementById('articleForm').style.display = 'none';
    document.getElementById('urlForm').style.display = 'block';
    document.getElementById('fileForm').style.display = 'none';
    document.getElementById('articleText').style.marginBottom = '0'; 
}


function showFileInput() {
    document.getElementById('articleForm').style.display = 'none';
    document.getElementById('urlForm').style.display = 'none';
    document.getElementById('fileForm').style.display = 'block';
    document.getElementById('articleText').style.marginBottom = '0'; 
}


document.getElementById('fileInput').addEventListener('change', function(event) {
    const fileName = event.target.files[0].name;
    document.getElementById('selectedFileName').textContent = fileName;
});




document.getElementById('articleForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const articleText = document.getElementById('articleText').value;

    fetch('http://localhost:8000/categorize', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: articleText })
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data); 
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


document.getElementById('urlForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const url = document.getElementById('articleUrl').value; 

    fetch('http://localhost:8000/scrape_and_classify', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});







document.getElementById('fileForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const file = document.getElementById('fileInput').files[0];

    if (file) {
        if (file.type === 'text/plain' || file.type === 'application/pdf') {
            readFileContent(file)
                .then(data => {
                    fetch('http://localhost:8000/categorize', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ message: data })
                    })
                    .then(response => response.json())
                    .then(data => {
                        displayResults(data);
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        } else {
            console.error('Error: Unsupported file format. Please upload a text file (.txt) or a PDF file (.pdf).');
        }
    } else {
        console.error('Error: No file selected.');
    }
});


function readFileContent(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = function(event) {
            resolve(event.target.result);
        };
        reader.onerror = function(error) {
            reject(error);
        };
        if (file.type === 'application/pdf') {
            reader.readAsDataURL(file);
        } else {
            reader.readAsText(file);
        }
    });
}


function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    if (results.main_category) {
        resultsDiv.innerHTML += `<p><strong>Main Category:</strong> ${results.main_category} (${results.main_probability}%)</p>`;
        resultsDiv.innerHTML += '<p><strong>Subcategories:</strong></p>';
        resultsDiv.innerHTML += '<ul>';
        results.subcategories.forEach(category => {
            resultsDiv.innerHTML += `<li>${category[0]}: ${category[1]}%</li>`;
        });
        
        
        let totalPercentage = results.main_probability;
        results.subcategories.forEach(category => {
            totalPercentage += category[1];
        });

        
        const othersPercentage = 100 - totalPercentage;
        if (othersPercentage > 0) {
            resultsDiv.innerHTML += `<li>Others: ${othersPercentage}%</li>`;
        }
        resultsDiv.innerHTML += '</ul>';

        
        const categoryLabels = [results.main_category, ...results.subcategories.map(category => category[0]), 'Others'];
        const categoryPercentages = [results.main_probability, ...results.subcategories.map(category => category[1]), othersPercentage];
        const backgroundColors = getRandomColors(categoryLabels.length); 
        pieChart.data.labels = categoryLabels;
        pieChart.data.datasets[0].data = categoryPercentages;
        pieChart.data.datasets[0].backgroundColor = backgroundColors;
        pieChart.update();

      
        pieChart.options.title.text = `Category Distribution`;
        pieChart.update();
    } else {
        resultsDiv.innerHTML = '<p>Error: Unable to classify article.</p>';
    }
}


const ctx = document.getElementById('pieChart').getContext('2d');
pieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: [''],
        datasets: [{
            data: [0],
            backgroundColor: ['rgba(255, 99, 132, 0.7)'], 
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Category Distribution'
        }
    }
});


function getRandomColors(numColors) {
    const colors = [];
    for (let i = 0; i < numColors; i++) {
        const color = `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.7)`;
        colors.push(color);
    }
    return colors;
}
