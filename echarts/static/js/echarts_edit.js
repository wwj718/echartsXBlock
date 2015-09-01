/* Javascript for echartsXBlock. */
function echartsXBlockInitStudio(runtime, element) {

    editor = CodeMirror.fromTextArea(
    document.getElementById("echarts_edit_echarts_data"),
    { lineNumbers: true }
    );
    var echarts_data = $("#echarts_edit_echarts_data").attr("data");
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
            'display_name': $('#echarts_edit_display_name').val(),
            'echarts_data': editor.getValue(),
            'file_id': $('#echarts_edit_file_id').val(),
            'app_id': $('#echarts_edit_app_id').val(),
            'width': $('#echarts_edit_width').val(),
            'height': $('#echarts_edit_height').val(),
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
    (new Function(editor.doc.getValue()))();
    myChart.setOption(option);
    //myChart.setTheme(e_macarons);
	console.log(data);
}
