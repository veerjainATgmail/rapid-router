/**
 * Created by ruth.wall on 19/08/2015.
 */

var ocargo = ocargo || {};

ocargo.LevelEditor.State = {

    applyAlongStrike : function(func, strikeEnd) {
        var x, y,
            strikeStart = ocargo.LEconfig.strikeStart;
        if (!strikeStart) {
            return;
        }

        if (strikeStart.x <= strikeEnd.x) {
            for (x = strikeStart.x; x <= strikeEnd.x; x++) {
                func(x, strikeStart.y);
            }
        } else {
            for (x = strikeStart.x; x >= strikeEnd.x; x--) {
                func(x, strikeStart.y);
            }
        }

        if (strikeStart.y <= strikeEnd.y) {
            for (y = strikeStart.y + 1; y <= strikeEnd.y; y++) {
                func(strikeEnd.x, y);
            }
        } else {
            for (y = strikeStart.y - 1; y >= strikeEnd.y; y--) {
                func(strikeEnd.x, y);
            }
        }
    }

}

