/* Javascript for echartsXBlock. */
function echartsXBlockInitStudio(runtime, element) {

    $(element).find('.action-cancel').bind('click', function() {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function() {
        var data = {
            'display_name': $('#echarts_edit_display_name').val(),
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
