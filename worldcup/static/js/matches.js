
console.log("moi");
var addMatches = function(groupIndex) {
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
        console.log(groupIndex);
        console.log(indexToChar.charAt(groupIndex));
        console.log(groups[indexToChar.charAt(groupIndex)]);
        html += '<div class="panel panel-default">' +
                '<div class="panel-heading middle" style="font-size: 30px; color: red">GROUP ' + indexToChar.charAt(groupIndex).toUpperCase() + '</div>' +
                '<ul class="list-group panel-body" style="padding: 0;">';
        groups[indexToChar.charAt(groupIndex)]['matches'].forEach( function(match, index) {
            html +=
                '<li class="list-group-item"> ' +
                    '<p class="middle" style="font-size: 20px">' +
                        teams[match["home_team"] - 1]["name"] + ' - ' +
                        teams[match["away_team"] - 1]["name"] +
                    '</p>' +
                    '<div class="middle">' +
                    '<input class="save-points"></input>' + ' - ' +
                    '<textarea class="save-points" rows="1" cols="2"> </textarea>' +
                    '</div>' +
                '</li>';

        });
        html += '</ul>' +
                '</div>' +
                '</div>';
        matchList.append(html);


    });

}
$(document).ready(function () {
    //console.log("document ready");
    for (var groupIndex = 0; groupIndex < 8; groupIndex++) {
        //console.log(groupIndex);
        addMatches(groupIndex);
    }

});

