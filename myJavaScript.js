var vg_1 = "IndustriesC02Graph.vl.json";
var vg_2 = "CountryCO2Map.vl.json";
vegaEmbed("#area_chart", vg_1).then(function (result) { }).catch(console.error);
vegaEmbed("#map", vg_2).then(function (result) { }).catch(console.error);