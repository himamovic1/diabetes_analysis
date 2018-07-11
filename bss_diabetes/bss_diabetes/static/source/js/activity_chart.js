let activityChart = {
    render: function (ctx, data_active, data_inactive) {
        const config = {
            type: 'line',
            data: {
                labels: ['Prije doručka', 'Nakon doručka', 'Prije ručka', 'Nakon ručka', 'Prije večere', 'Nakon večere'],
                datasets: [{
                    label: 'Fizički aktivni',
                    data: data_active,
                    borderColor: window.chartColors.blue,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: false,
                }, {
                    label: 'Fizički neaktivni',
                    data: data_inactive,
                    borderColor: window.chartColors.red,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: false,
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Komparacija fizički aktivnih i fizički neaktivnih pacijenata'
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
                            labelString: 'Value'
                        },
                        ticks: {
                            suggestedMin: 5,
                            suggestedMax: 15,
                        }
                    }]
                }
            }
        };

        return new Chart(ctx, config);
    }
};

export {activityChart};
