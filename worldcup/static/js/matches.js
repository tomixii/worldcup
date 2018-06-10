var groupIndex = 0;
var addMatches = function() {
    $.getJSON("https://raw.githubusercontent.com/lsv/fifa-worldcup-2018/master/data.json", function(data) {
        var groups = data['groups'];
        var teams = data['teams'];
        var matches = [];
        var indexToChar = "abcdefgh";
        var matchList = $('#match-list');
        var html = ""
        $.each(groups, function(c, info) {
            matches.push.apply(matches, info['matches']);
        });

        html += '<div class="row">' +
                '<div class="col-sm-3">';
        if (groupIndex !== 0) {
            html += '<i id="left-arrow" class="fas fa-angle-left fa-9x" style="color: white"></i>';
        }
        html += '</div>' +
                '<div class="panel panel-default col-sm-6">' +
                '<div class="panel-heading middle" style="font-size: 30px; color: red">GROUP ' + indexToChar[groupIndex].toUpperCase() + '</div>' +
                '<ul class="list-group panel-body" style="padding: 0;">';
        groups[indexToChar[groupIndex]]['matches'].forEach( function(match, index) {
            html +=
                '<li class="list-group-item"> ' +
                    '<p class="middle" style="font-size: 20px">' +
                        teams[match["home_team"] - 1]["name"] + ' - ' +
                        teams[match["away_team"] - 1]["name"] +
                    '</p>' +
                '</li>';

        });
        html += '</ul>' +
                '</div>' +
                '<div class="col-sm-3">';
        if (groupIndex < 7) {
            html += '<i id="right-arrow" class="fas fa-angle-right fa-9x" style="color: white"></i>';
        }
        html += '</div></div>';
        matchList.append(html);
    });

}
$(document).ready(function () {
    console.log("ready");
    console.log($('#left-arrow'))
    $('#left-arrow').click( function() {
        console.log("left arrow");
        groupIndex--;
        addMatches();
    });
    console.log($('#right-arrow'))
    $('#right-arrow').click( function() {
        console.log("right arrow");
        groupIndex++;
        addMatches();
    });

});

window.onload = function() {
    addMatches();
}
