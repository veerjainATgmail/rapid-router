'use strict';

var ocargo = ocargo || {};

ocargo.LevelEditor.Mark = {

    /************/
    /*  Marking */
    /************/
    // Methods for highlighting squares

    mark : function(coordMap, colour, opacity) {
        var coordPaper = ocargo.Drawing.translate(coordMap);
        var element = ocargo.LEconfig.grid[coordPaper.x][coordPaper.y];
        element.attr({fill:colour, "fill-opacity": opacity});
    },

    markAsOrigin : function(coordinate) {
        this.mark(coordinate, 'red', 0.7, true);
    },

    markAsDestination : function(coordinate) {
        this.mark(coordinate, 'blue', 0.7, true);
    },

    markAsBackground : function(coordinate, currentTheme) {
        this.mark(coordinate, currentTheme.background, 0, false);
    },

    markAsHighlighted : function(coordinate, currentTheme) {
        this.mark(coordinate, currentTheme.selected, 0.3, true);
    },

    markAsSelected : function(coordinate, currentTheme) {
        this.mark(coordinate, currentTheme.selected, 1, true);
    },

    clearMarkings : function(currentTheme) {
        for (var i = 0; i < GRID_WIDTH; i++) {
            for (var j = 0; j < GRID_HEIGHT; j++) {
                this.markAsBackground(new ocargo.Coordinate(i,j), currentTheme);
                ocargo.LEconfig.grid[i][j].toFront();
            }
        }
        if (ocargo.LEconfig.originNode) {
            this.markAsOrigin(ocargo.LEconfig.originNode.coordinate);
        }
        if (ocargo.LEconfig.destinationNode) {
            this.markAsDestination(ocargo.LEconfig.destinationNode.coordinate);
        }

        ocargo.LevelEditor.render.bringTrafficLightsToFront();
        ocargo.LevelEditor.render.bringDecorToFront();
    },

    markTentativeRoad : function(currentEnd,currentTheme) {
        this.clearMarkings(currentTheme);
        ocargo.LevelEditor.State.applyAlongStrike(setup, currentEnd);

        var previousNode = null;
        function setup(x, y) {
            var coordinate = new ocargo.Coordinate(x, y);
            var node = new ocargo.Node(coordinate);
            if (previousNode) {
                node.addConnectedNodeWithBacklink(previousNode);
            }
            previousNode = node;
            ocargo.LevelEditor.Mark.markAsSelected(coordinate, currentTheme);
        }
    }
}