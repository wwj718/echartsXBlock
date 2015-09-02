/* Javascript for echartsXBlock. */
function echartsXBlockInitView(runtime, element) {
    /* Weird behaviour :
     * In the LMS, element is the DOM container.
     * In the CMS, element is the jQuery object associated*
     * So here I make sure element is the jQuery object */
     //get params from studio
     //get_params(runtime, element);
    var echarts_data = $(element).find(".echarts_edit_echarts_data").attr("data");
    //console.log("mytest");
    var main = $(element).find('.echarts_div')[0];
    var myChart = echarts.init(main);
    (new Function(echarts_data))();
    myChart.setOption(option);
    //myChart.setTheme(e_macarons);
	console.log(echarts_data);
}

