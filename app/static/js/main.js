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
                console.log(data.result);
            }
        })
    });
});