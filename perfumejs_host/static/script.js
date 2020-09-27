$(document).ready(()=>{
    $.ajax({
        url: "http://google.com",
        type: "GET",
        crossDomain: true,
        success: function (response) {
            console.log("DA", response)
        },
        error: function(xhr, status) {
            console.log(xhr, status)
        }
    })
})