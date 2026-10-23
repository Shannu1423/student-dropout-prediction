// Chart.js initialization for Sanskriti University Dropout Prediction Dashboard

document.addEventListener('DOMContentLoaded', function () {
    fetch('/api/analytics')
        .then(response => response.json())
        .then(data => {
            renderRiskDistribution(data.risk_distribution);
            renderDepartmentRisk(data.department_distribution);
            renderAttendanceRisk(data.attendance_risk);
        })
        .catch(err => {
            console.error('Error fetching analytics data:', err);
        });
});

function renderRiskDistribution(riskData) {
    const ctx = document.getElementById('riskDistributionChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: riskData.labels,
            datasets: [{
                data: riskData.data,
                backgroundColor: ['#10b981', '#ef4444'],
                hoverOffset: 4,
                borderWidth: 2,
                borderColor: '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            cutout: '70%'
        }
    });
}

function renderDepartmentRisk(deptData) {
    const ctx = document.getElementById('departmentRiskChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: deptData.labels,
            datasets: [
                {
                    label: 'At Risk Students',
                    data: deptData.at_risk,
                    backgroundColor: '#ef4444',
                    borderRadius: 4
                },
                {
                    label: 'Total Monitored',
                    data: deptData.total,
                    backgroundColor: '#94a3b8',
                    borderRadius: 4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    grid: { display: false },
                    ticks: {
                        callback: function(val, index) {
                            const lbl = this.getLabelForValue(val);
                            return lbl.length > 12 ? lbl.substr(0, 10) + '...' : lbl;
                        },
                        font: { size: 10 }
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: { stepSize: 1 }
                }
            },
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { boxWidth: 12, font: { size: 11 } }
                }
            }
        }
    });
}

function renderAttendanceRisk(attData) {
    const ctx = document.getElementById('attendanceRiskChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: attData.labels,
            datasets: [{
                label: 'At-Risk Count',
                data: attData.data,
                backgroundColor: [
                    '#b91c1c',
                    '#ef4444',
                    '#f59e0b',
                    '#3b82f6',
                    '#10b981'
                ],
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: { grid: { display: false }, ticks: { font: { size: 11 } } },
                y: { beginAtZero: true, ticks: { stepSize: 1 } }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}
