const Highcharts = require('highcharts');

require('highcharts/modules/exporting')(Highcharts);

Highcharts.chart('container', {
  chart: { type: 'bar' },
  title: { text: 'Fruit Consumption' },
  xAxis: { categories: ['Apples', 'Bananas', 'Oranges'] },
  yAxis: { title: { text: 'Fruit eaten' } },
  series: [
    { name: 'Jane', data: [1, 0, 4] },
    { name: 'John', data: [5, 7, 3] } ]
});

// Highmaps モジュールと北米の地図データの読み込み
require('highcharts/modules/map')(Highcharts);
const north_america_no_central = require('@highcharts/map-collection/custom/north-america-no-central.geo.json')

// 北米の地図にのせるデータの設定（内容に意味はない）
const data = [
  //{ 'hc-key': 'us', value: 3 },
  //{ 'hc-key': 'ca', value: 5 },
  { 'hc-key': 'mx', value: 20 } ];

Highcharts.mapChart('world_map', {
  chart: { map: north_america_no_central },
  title: { text: 'World Map' },
  countryData: [ { key: 'in', index: 2 }, { key: 'us', index: 2 } ],
  colorAxis: { min: 0 },
  series: [
    { data: data,
      mapData: north_america_no_central,
      joinBy: 'hc-key',
      allAreas: false,
      name: 'Random data',
      dataLabels: { enabled: true, format: '{point.name}' }
    } ]
});
