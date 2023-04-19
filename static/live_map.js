var chartCPU;
var chartGPU;

function requestData()
{
    // Ajax call to get the Data from Flask

    // change API here to the variable of IP

    var requests = $.get('/sensors');

    var tm = requests.done(function (result)
    {
        // CPU
        var seriesCPU = chartCPU.series[0],
            shiftCPU = seriesCPU.data.length > 100;

        // GPU
        var seriesGPU = chartGPU.series[0],
            shiftGPU = seriesGPU.data.length > 100;

        // HDD
        var seriesHDD = chartHDD.series[0],
            shiftHDD = seriesHDD.data.length > 100;

        // Add the Point
        // Time CPU
        var data1 = [];
        data1.push(result.time);
        data1.push(result.cpu_temp);

        // Add the Point
        // Time GPU
        var data2 = [];
        data2.push(result.time);
        data2.push(result.gpu_temp);

        // Add the Point
        // Time HDD
        var data3 = [];
        data3.push(result.time);
        data3.push(result.disk_temp);

        chartCPU.series[0].addPoint(data1, true, shiftCPU);
        chartGPU.series[0].addPoint(data2, true, shiftGPU);
        chartHDD.series[0].addPoint(data3, true, shiftHDD);

        $(".sensor1").text("");
        $(".sensor1").text("CPU : " +  Math.round(data1[1]) );

        $(".sensor2").text("");
        $(".sensor2").text("GPU : " +  Math.round(data2[1]) );

        $(".sensor3").text("");
        $(".sensor3").text("HDD : " +  Math.round(data3[1]) );

        // call it again after one second
        setTimeout(requestData, interval*1000);

    });
}

$(document).ready(function()
{
    // --------------Chart 1 ----------------------------
    chartCPU = new Highcharts.Chart({
        chart:
            {
            height: 250,
            renderTo: 'data-cpu',
            defaultSeriesType: 'area',
            events: {
                load: requestData
                    }
            },
        title:
            {
            text: ''
            },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 100,
            maxZoom: 20 * 1000
                },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Temp',
                margin: 80
                    }
                 },
        series: [{
            color : '#c23d23',
            lineColor: '#303030',
            name: 'CPU',
            data: []
        }]
    });
    // --------------Chart 1 Ends - -----------------

    chartGPU = new Highcharts.Chart({
        chart:
            {
                height: 250,
                renderTo: 'data-gpu',
                defaultSeriesType: 'area',
                events: {
                    load: requestData
                }
            },
        title:
            {
                text: ''
            },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 100,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Temp',
                margin: 80
            }
        },
        series: [{
            lineColor: '#1d82b8',
            name: 'GPU',
            data: []
        }]
    });

    chartHDD = new Highcharts.Chart({
        chart:
            {
                height: 250,
                renderTo: 'data-hdd',
                defaultSeriesType: 'area',
                events: {
                    load: requestData
                }
            },
        title:
            {
                text: ''
            },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 100,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Temp',
                margin: 80
            }
        },
        series: [{
            lineColor: '#22882c',
            color: '#7ee627',
            name: 'HDD',
            data: []
        }]
    });

});