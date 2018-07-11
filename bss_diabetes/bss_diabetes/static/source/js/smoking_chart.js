let smokingChart = {
    render: function (ctx, data_values) {
        const config = {
            type: 'bar',
            data: {
                labels: ['Bez dijabetesa', 'Sa dijabetesom'],
                datasets: [{
                    label: 'Broj bivših pušača',
                    data: data_values,
                    backgroundColor: 'rgba(66, 149, 244, 50)',
                    fill: true,
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Pregled broja dijabetičara nakon prestanka pušenja'
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
                            labelString: 'Broj pacijenata'
                        },
                        ticks: {
                            suggestedMin: 10,
                            suggestedMax: 40,
                        }
                    }]
                }
            }
        };
        let chart = new Chart(ctx, config);

        return chart;
    }
};

export {smokingChart};
