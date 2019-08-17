advice_url = "https://sf-pyw.mosyag.in/m04/api/forecasts"
function take_predict() {
    $.getJSON(advice_url, function(data) {
        $.each(data["prophecies"], function(i, d) {
            p = $("#p-" + i)
            p.html("<p>" + d + "</p>")
        })
    })
}