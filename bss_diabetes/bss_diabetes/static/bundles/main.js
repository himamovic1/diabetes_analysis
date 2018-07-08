import "file-loader:../../../node_modules/chart.js/dist/Chart.bundle.js";

import {homeCharts} from "../source/js/home_chart";
import {dietCharts} from "../source/js/diet_chart";
import {activityChart} from "../source/js/activity_chart";

let charts = {
    home: homeCharts,
    diet: dietCharts,
    activity: activityChart
};

export {charts};