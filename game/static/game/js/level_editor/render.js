/**
 * Created by ruth.wall on 19/08/2015.
 */

var ocargo = ocargo || {};

ocargo.LevelEditor.render = {

    trafficLights : ocargo.LEconfig.trafficLights,
    decor : ocargo.LEconfig.decor,

    bringTrafficLightsToFront : function() {
        var trafficLights = this.trafficLights;

        for (var i = 0; i < trafficLights.length; i++) {
            trafficLights[i].image.toFront();
        }
    },

    bringDecorToFront : function() {
        var decor = this.decor;

        for (var i = 0; i < decor.length; i++) {
            decor[i].image.toFront();
        }
    }

}

