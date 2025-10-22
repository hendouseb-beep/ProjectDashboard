fetch('/data')
.then(response => response.json())
.then(data => {
    const ctx = document.getElementById('statusChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Projets par statut',
                data: Object.values(data),
                backgroundColor: ['#f39c12','#2ecc71','#e74c3c']
            }]
        }
    });
});
