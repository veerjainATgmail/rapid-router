'use strict';

var ocargo = ocargo || {};

ocargo.LevelEditor.AddRemoveRoad = {
    handleMouseDown : function(coordMap){
        ocargo.LEconfig.strikeStart = coordMap;
        ocargo.LevelEditor.Mark.markAsSelected(coordMap, ocargo.LEconfig.currentTheme);
    }
}