let diabetesHistoryChart = {
    render: function (ctx, data_values) {
        const config = {
            type: 'bar',
            data: {
                labels: ['Nema historije diabetisa', 'Postoji historija diabetisa'],
                datasets: [{
                    label: 'Broj dijabetičara',
                    data: data_values,
                    backgroundColor: 'rgba(66, 149, 244, 50)',
                    fill: true,
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Pregled broja pacijenata sa historijom diabetisa'
                },
                tooltips: {
                    mode: 'index'
                },
                scales: {
                    xAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true
                        }
                    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Broj dijabetičara'
                        },
                        ticks: {
                            suggestedMin: 10,
                            suggestedMax: 80,
                        }
                    }]
                }
            }
        };
        let chart = new Chart(ctx, config);

        return chart;
    }
};

export {diabetesHistoryChart};
