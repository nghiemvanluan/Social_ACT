function getChartColorsArray(e) {
  if (null !== document.getElementById(e)) {
    var t = document.getElementById(e).getAttribute("data-colors");
    if (t)
      return (t = JSON.parse(t)).map(function (e) {
        var t = e.replace(" ", "");
        if (-1 === t.indexOf(",")) {
          var o = getComputedStyle(document.documentElement).getPropertyValue(
            t
          );
          return o || t;
        }
        e = e.split(",");
        return 2 != e.length
          ? t
          : "rgba(" +
              getComputedStyle(document.documentElement).getPropertyValue(
                e[0]
              ) +
              "," +
              e[1] +
              ")";
      });
    console.warn("data-colors atributes not found on", e);
  }
}
var worldlinemap,
  vectorMapWorldLineColors = getChartColorsArray("users-by-country");
vectorMapWorldLineColors &&
  (worldlinemap = new jsVectorMap({
    map: "world_merc",
    selector: "#users-by-country",
    zoomOnScroll: !1,
    zoomButtons: !1,
    markers: [
      { name: "Greenland", coords: [72, -42] },
      { name: "Canada", coords: [56.1304, -106.3468] },
      { name: "Brazil", coords: [-14.235, -51.9253] },
      { name: "Egypt", coords: [26.8206, 30.8025] },
      { name: "Russia", coords: [61, 105] },
      { name: "China", coords: [35.8617, 104.1954] },
      { name: "United States", coords: [37.0902, -95.7129] },
      { name: "Norway", coords: [60.472024, 8.468946] },
      { name: "Ukraine", coords: [48.379433, 31.16558] },
    ],
    lines: [
      { from: "Canada", to: "Egypt" },
      { from: "Russia", to: "Egypt" },
      { from: "Greenland", to: "Egypt" },
      { from: "Brazil", to: "Egypt" },
      { from: "United States", to: "Egypt" },
      { from: "China", to: "Egypt" },
      { from: "Norway", to: "Egypt" },
      { from: "Ukraine", to: "Egypt" },
    ],
    regionStyle: {
      initial: {
        stroke: "#9599ad",
        strokeWidth: 0.25,
        fill: vectorMapWorldLineColors,
        fillOpacity: 1,
      },
    },
    lineStyle: { animation: !0, strokeDasharray: "6 3 6" },
  }));

var barchartCountriesColors = getChartColorsArray("countries_charts");
var genders_0 = document.getElementById("genders_0").innerText;
var genders_1 = document.getElementById("genders_1").innerText;
function generateData(e, t) {
  for (var o = 0, a = []; o < e; ) {
    var r = (o + 1).toString() + "h",
      s = Math.floor(Math.random() * (t.max - t.min + 1)) + t.min;
    a.push({ x: r, y: s }), o++;
  }
  return a;
}
barchartCountriesColors &&
  ((options = {
    series: [
      {
        data: [parseInt(genders_0), parseInt(genders_1)],
        name: "",
      },
    ],
    chart: { type: "bar", toolbar: { show: !1 } },
    plotOptions: {
      bar: {
        borderRadius: 4,
        horizontal: !0,
        distributed: !0,
        dataLabels: { position: "top" },
      },
    },
    colors: barchartCountriesColors,
    dataLabels: {
      enabled: !0,
      offsetX: 32,
      style: { fontSize: "12px", fontWeight: 400, colors: ["#212529"] },
    },
    legend: { show: !1 },
    grid: { show: !1 },
    xaxis: {
      categories: ["Nam", "Nữ"],
    },
  }),
  (chart = new ApexCharts(
    document.querySelector("#countries_charts"),
    options
  )).render());
// ----------------------
var marital_status_0 = document.getElementById("marital_status_0").innerText;
var marital_status_1 = document.getElementById("marital_status_1").innerText;
var barchartCountriesColors = getChartColorsArray("countries_chartsHN");
function generateData(e, t) {
  for (var o = 0, a = []; o < e; ) {
    var r = (o + 1).toString() + "h",
      s = Math.floor(Math.random() * (t.max - t.min + 1)) + t.min;
    a.push({ x: r, y: s }), o++;
  }
  return a;
}
barchartCountriesColors &&
  ((options = {
    series: [
      {
        data: [parseInt(marital_status_0), parseInt(marital_status_1)],
        name: "",
      },
    ],
    chart: { type: "bar", toolbar: { show: !1 } },
    plotOptions: {
      bar: {
        borderRadius: 4,
        horizontal: !0,
        distributed: !0,
        dataLabels: { position: "top" },
      },
    },

    colors: barchartCountriesColors,
    dataLabels: {
      enabled: !0,
      offsetX: 32,
      style: { fontSize: "12px", fontWeight: 400, colors: ["#212529"] },
    },
    legend: { show: !1 },
    grid: { show: !1 },
    xaxis: {
      categories: ["ĐKH", "CKH"],
    },
  }),
  (chart = new ApexCharts(
    document.querySelector("#countries_chartsHN"),
    options
  )).render());

// --------------------
var chartHeatMapBasicColors = getChartColorsArray(
  "audiences-sessions-country-charts"
);
chartHeatMapBasicColors &&
  ((options = {
    series: [
      { name: "Sat", data: generateData(18, { min: 0, max: 90 }) },
      { name: "Fri", data: generateData(18, { min: 0, max: 90 }) },
      { name: "Thu", data: generateData(18, { min: 0, max: 90 }) },
      { name: "Wed", data: generateData(18, { min: 0, max: 90 }) },
      { name: "Tue", data: generateData(18, { min: 0, max: 90 }) },
      { name: "Mon", data: generateData(18, { min: 0, max: 90 }) },
      { name: "Sun", data: generateData(18, { min: 0, max: 90 }) },
    ],
    chart: {
      height: 400,
      type: "heatmap",
      offsetX: 0,
      offsetY: -8,
      toolbar: { show: !1 },
    },
    plotOptions: {
      heatmap: {
        colorScale: {
          ranges: [
            { from: 0, to: 50, color: chartHeatMapBasicColors[0] },
            { from: 51, to: 100, color: chartHeatMapBasicColors[1] },
          ],
        },
      },
    },
    dataLabels: { enabled: !1 },
    legend: {
      show: !0,
      horizontalAlign: "center",
      offsetX: 0,
      offsetY: 20,
      markers: { width: 20, height: 6, radius: 2 },
      itemMargin: { horizontal: 12, vertical: 0 },
    },
    colors: chartHeatMapBasicColors,
    tooltip: {
      y: [
        {
          formatter: function (e) {
            return void 0 !== e ? e.toFixed(0) + "k" : e;
          },
        },
      ],
    },
  }),
  (chart = new ApexCharts(
    document.querySelector("#audiences-sessions-country-charts"),
    options
  )).render());
var columnoptions,
  chartAudienceColumnChartsColors = getChartColorsArray(
    "audiences_metrics_charts"
  );
chartAudienceColumnChartsColors &&
  ((columnoptions = {
    series: [
      {
        name: "Last Year",
        data: [
          25.3, 12.5, 20.2, 18.5, 40.4, 25.4, 15.8, 22.3, 19.2, 25.3, 12.5,
          20.2,
        ],
      },
      {
        name: "Current Year",
        data: [
          36.2, 22.4, 38.2, 30.5, 26.4, 30.4, 20.2, 29.6, 10.9, 36.2, 22.4,
          38.2,
        ],
      },
    ],
    chart: { type: "bar", height: 309, stacked: !0, toolbar: { show: !1 } },
    plotOptions: {
      bar: { horizontal: !1, columnWidth: "20%", borderRadius: 6 },
    },
    dataLabels: { enabled: !1 },
    legend: {
      show: !0,
      position: "bottom",
      horizontalAlign: "center",
      fontWeight: 400,
      fontSize: "8px",
      offsetX: 0,
      offsetY: 0,
      markers: { width: 9, height: 9, radius: 4 },
    },
    stroke: { show: !0, width: 2, colors: ["transparent"] },
    grid: { show: !1 },
    colors: chartAudienceColumnChartsColors,
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
      ],
      axisTicks: { show: !1 },
      axisBorder: {
        show: !0,
        strokeDashArray: 1,
        height: 1,
        width: "100%",
        offsetX: 0,
        offsetY: 0,
      },
    },
    yaxis: { show: !1 },
    fill: { opacity: 1 },
  }),
  (chart = new ApexCharts(
    document.querySelector("#audiences_metrics_charts"),
    columnoptions
  )).render());

const educational_attainment_0 = document.getElementById(
  "educational_attainment_0"
).innerText;
const educational_attainment_1 = document.getElementById(
  "educational_attainment_1"
).innerText;
const educational_attainment_2 = document.getElementById(
  "educational_attainment_2"
).innerText;
const educational_attainment_3 = document.getElementById(
  "educational_attainment_3"
).innerText;
var options,
  chart,
  dountchartUserDeviceColors = getChartColorsArray("user_device_pie_charts");
dountchartUserDeviceColors &&
  ((options = {
    series: [
      parseInt(educational_attainment_0),
      parseInt(educational_attainment_1),
      parseInt(educational_attainment_2),
      parseInt(educational_attainment_3),
    ],
    labels: ["HS-SV", "Cử nhân", "Sau đại học", "Chuyên gia"],
    chart: { type: "donut", height: 219 },
    plotOptions: { pie: { size: 100, donut: { size: "76%" } } },
    dataLabels: { enabled: !1 },
    legend: {
      show: !1,
      position: "bottom",
      horizontalAlign: "center",
      offsetX: 0,
      offsetY: 0,
      markers: { width: 20, height: 6, radius: 2 },
      itemMargin: { horizontal: 12, vertical: 0 },
    },
    stroke: { width: 0 },
    yaxis: {
      labels: {
        formatter: function (e) {
          return e + " Người";
        },
      },
      tickAmount: 4,
      min: 0,
    },
    colors: dountchartUserDeviceColors,
  }),
  (chart = new ApexCharts(
    document.querySelector("#user_device_pie_charts"),
    options
  )).render());

const job_0 = document.getElementById("job_0").innerText;
const job_1 = document.getElementById("job_1").innerText;
const job_2 = document.getElementById("job_2").innerText;
const job_3 = document.getElementById("job_3").innerText;
const job_4 = document.getElementById("job_4").innerText;

dountchartUserDeviceColors = getChartColorsArray("user_device_pie_chartsNN");
dountchartUserDeviceColors &&
  ((options = {
    series: [
      // parseInt(job_0),
      // parseInt(job_1),
      // parseInt(job_2),
      // parseInt(job_3),
      // parseInt(job_4),
      1, 2, 3, 4, 5,
    ],
    labels: ["HS-SV", "Thực tập sinh", "Mới đi làm", "Quản lý", "Điều hành"],
    chart: { type: "donut", height: 219 },
    plotOptions: { pie: { size: 100, donut: { size: "76%" } } },
    dataLabels: { enabled: !1 },
    legend: {
      show: !1,
      position: "bottom",
      horizontalAlign: "center",
      offsetX: 0,
      offsetY: 0,
      markers: { width: 20, height: 6, radius: 2 },
      itemMargin: { horizontal: 12, vertical: 0 },
    },
    stroke: { width: 0 },
    yaxis: {
      labels: {
        formatter: function (e) {
          return e + " Người";
        },
      },
      tickAmount: 4,
      min: 0,
    },
    colors: dountchartUserDeviceColors,
  }),
  (chart = new ApexCharts(
    document.querySelector("#user_device_pie_chartsNN"),
    options
  )).render());
