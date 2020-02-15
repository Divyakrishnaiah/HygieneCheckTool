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
                console.log(data.result);
            }
        })
    });
});