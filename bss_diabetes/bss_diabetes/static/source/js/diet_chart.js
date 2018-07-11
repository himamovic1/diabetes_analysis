let dietCharts = {
    render: function (ctx, bellowAverage, average, aboveAverage) {
        const config = {
            type: 'line',
            data: {
                labels: ['Prije doručka', 'Nakon doručka', 'Prije ručka', 'Nakon ručka', 'Prije večere', 'Nakon večere'],
                datasets: [{
                    label: 'Manje nego inače',
                    data: bellowAverage,
                    borderColor: window.chartColors.blue,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: false,
                }, {
                    label: 'Standarno',
                    data: average,
                    borderColor: window.chartColors.green,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: false,
                }, {
                    label: 'Više nego inače',
                    data: aboveAverage,
                    borderColor: window.chartColors.red,
                    backgroundColor: 'rgba(0, 0, 0, 0)',
                    fill: false,
                }]
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Komparacija količine glukoze u krvi relativno na prehrambene navike'
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
                            labelString: 'Koncentracija glukoze (mmol/L)'
                        },
                        ticks: {
                            suggestedMin: 7,
                            suggestedMax: 12,
                        }
                    }]
                }
            }
        };

        return new Chart(ctx, config);
    }
};

export {dietCharts};
