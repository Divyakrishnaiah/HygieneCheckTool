$(document).ready(function() {
    $("#compare").click(function(event) {
        $.ajax({
            data : {
                include : $("#incSyx").val(),
                exclude : $("#exSyx").val()
            },
            type : 'POST',
            url : '/compare',
            success : function(data) {
                data = JSON.parse(data)
                $('#result').val(data.result)
                $('#result').css('height','90%')
            }
        })
    });

    $("#fmissing").click(function(event) {
        $.ajax({
            data : {
                dockeys : $('#docKwds').val(),
                modelsyx : $('#msSyx').val()
            },
            type : 'POST',
            url : '/getmissingkeys',
            success : function(data) {
                data = JSON.parse(data);
                $('#mresult').val(data.result)
                $('#mresult').css('height', '90%')
            }
        })
    });
});