
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
        html += '<div class="row">' +
                '<div class="panel panel-default col-md-6 col-md-offset-3">' +
                '<div class="panel-heading middle" style="font-size: 30px; color: red">GROUP ' + indexToChar.charAt(groupIndex).toUpperCase() + '</div>' +
                '<ul class="list-group panel-body" style="padding: 0;">';
        groups[indexToChar.charAt(groupIndex)]['matches'].forEach( function(match, index) {
            html +=
                '<li class="list-group-item"> ' +
                    '<p class="middle" style="font-size: 20px">' +
                        teams[match["home_team"] - 1]["name"] + ' - ' +
                        teams[match["away_team"] - 1]["name"] +
                    '</p>' +
                    '<div class="middle row">' +
                    '<input id="home_'+ match.id + '" class="save-points" +
                    'type="number"></input>' + ' - ' +
                    '<input id="away_'+ match.id + '" class="save-points" +
                    'type="number"></input>' +
                    '</div>' +
                '</li>';

        });
        html += '</ul>' +
                '</div>' +
                '</div>' +
                '</div>' +
                '<input id="save-btn" class="btn-primary middle" +
                'type="submit"></input>';
        matchList.append(html);


    });

}
$(document).ready(function () {
    //console.log("document ready");
    for (var groupIndex = 0; groupIndex < 8; groupIndex++) {
        //console.log(groupIndex);
        addMatches(groupIndex);
    }

    $('#save-btn').on('click', function() {
        database = {};
        for (var i = 1; i <= 64; i++) {
            var home_score = $('#home_' + i).val();
            var away_score = $('#away_' + i).val();
            database += { i:
            }
        }
    });

});

