/* Javascript for echartsXBlock. */
function echartsXBlockInitStudio(runtime, element) {
    editor = CodeMirror.fromTextArea(
    document.getElementById("echarts_edit_echarts_data_textarea"),
    { lineNumbers: true }
    );
    var echarts_data = $(element).find("#echarts_data").attr("data");
    editor.setValue(echarts_data);

    $(element).find('#build_echart').bind('click', function() {
	data = editor.getValue();
	build_echart(data);
    });


    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $(element).find('#echarts_edit_display_name').val(),
            'echarts_data': editor.getValue()
       };

        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'save_echarts');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                // window.location.reload(false);
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}

function build_echart(data){
    var myChart = echarts.init(document.getElementById('main'));
    var option = (new Function(editor.doc.getValue()))();
    myChart.setOption(option);
    //myChart.setTheme(e_macarons);
	console.log(data);
}
