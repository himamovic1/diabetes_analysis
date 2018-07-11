import "file-loader:../../../node_modules/chart.js/dist/Chart.bundle.js";
import "../source/js/chartUtils"

import {homeCharts} from "../source/js/home_chart";
import {dietCharts} from "../source/js/diet_chart";
import {activityChart} from "../source/js/activity_chart";
import {ageChart} from '../source/js/age_chart';
import {smokingChart} from '../source/js/smoking_chart';

let charts = {
    home: homeCharts,
    diet: dietCharts,
    activity: activityChart,
    age: ageChart,
    smoking: smokingChart
};

export {charts};