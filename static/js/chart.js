
google.charts.load('current', {'packages':['line']});
google.charts.setOnLoadCallback(drawChart);
var count = 0;
var data;
var chart;
var options;

function drawChart() {
    console.log('test')
    console.log(areaArr)

    data = new google.visualization.DataTable();

    data.addColumn('string', '년/월');
    data.addColumn('number', '전기량');
    data.addColumn('number', '전기세');

    var options = {
    chart: {
        title: '쿨루프 시공 시 예상 전기량',
        subtitle: '전기 비용 감소 효과 기대'
    },
    width: 900,
    height: 500
    };

    var chart = new google.charts.Line(document.getElementById('linechart_material'));

    chart.draw(data, google.charts.Line.convertOptions(options));
}

function chartEnergy(areaArr) {
    console.log(areaArr)
    count++;
    data.addRows([
        ['201608', areaArr['electro_201608'], areaArr['electro_201608']],
        ['201708', areaArr['electro_201708'], areaArr['electro_201708']],
        ['201808', areaArr['electro_201808'], areaArr['electro_201808']],
        ['201908', areaArr['electro_201908'], areaArr['electro_201908']],
        ['202008', areaArr['electro_202008'], areaArr['electro_202008']],
        ['202108', areaArr['electro_202108'], areaArr['electro_202108']],
    ]);
    chart.draw(data, options)
}
function removeData(){
  data.removeRow(0);
  chart.draw(data, opstions)
}
