# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import models, migrations
from game.level_management import set_decor_inner, set_blocks_inner


def add_levels(apps, schema_editor):
    def set_decor(level, decor):
        set_decor_inner(level, decor, LevelDecor)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    Episode = apps.get_model('game', 'Episode')
    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    LevelBlock = apps.get_model('game', 'LevelBlock')
    Block = apps.get_model('game', 'Block')


    episode12 = Episode(pk=12, name="Cows", r_branchiness=0,
                        r_loopiness=0, r_num_tiles=10, r_curviness=0.5, r_pythonEnabled=0,
                        r_blocklyEnabled=1, r_trafficLights=0)
    episode12.save()

    episode11 = Episode.objects.get(pk=11)
    episode11.next_episode = episode12
    episode11.save()

    level110 = Level(
        name='110',
        episode=episode12,
        default=True,
        path='[{"coordinate":[1,5],"connectedNodes":[1]},{"coordinate":[2,5],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[4,4],"connectedNodes":[3,5]},{"coordinate":[4,3],"connectedNodes":[4,6]},{"coordinate":[5,3],"connectedNodes":[5,7]},{"coordinate":[6,3],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7,9]},{"coordinate":[7,2],"connectedNodes":[8,10]},{"coordinate":[8,2],"connectedNodes":[9]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":4,"y":3},{"x":6,"y":3},{"x":5,"y":3}],"type":"WHITE"}]',
        destinations='[[8,2]]',
        origin='{"coordinate":[1,5],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution=[6],
    )
    level110.save()
    set_decor(level110, json.loads('[{"x":530,"y":385,"z":4,"decorName":"tree1"},{"x":323,"y":495,"z":4,"decorName":"tree1"},{"x":324,"y":266,"z":4,"decorName":"tree1"},{"x":726,"y":289,"z":4,"decorName":"tree1"},{"x":511,"y":157,"z":4,"decorName":"tree1"}]'))
    set_blocks(level110, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"declare_event"},{"type":"puff_up"},{"type":"sound_horn"}]'))

    level111 = Level(
        name='111',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,6],"connectedNodes":[5]},{"coordinate":[2,6],"connectedNodes":[5,6]},{"coordinate":[3,5],"connectedNodes":[9,10,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,3],"connectedNodes":[8,3]},{"coordinate":[1,6],"connectedNodes":[0,1]},{"coordinate":[2,5],"connectedNodes":[1,7]},{"coordinate":[2,4],"connectedNodes":[6,8]},{"coordinate":[2,3],"connectedNodes":[7,4]},{"coordinate":[3,6],"connectedNodes":[2]},{"coordinate":[4,5],"connectedNodes":[2,11]},{"coordinate":[4,4],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[4,2],"connectedNodes":[12,14,25]},{"coordinate":[5,2],"connectedNodes":[13,15]},{"coordinate":[5,3],"connectedNodes":[16,14]},{"coordinate":[5,4],"connectedNodes":[26,17,15]},{"coordinate":[6,4],"connectedNodes":[16,18]},{"coordinate":[6,3],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[6,1],"connectedNodes":[19,21,27]},{"coordinate":[7,1],"connectedNodes":[20,22]},{"coordinate":[7,2],"connectedNodes":[23,21]},{"coordinate":[7,3],"connectedNodes":[24,22]},{"coordinate":[8,3],"connectedNodes":[23]},{"coordinate":[4,1],"connectedNodes":[13]},{"coordinate":[5,5],"connectedNodes":[16]},{"coordinate":[6,0],"connectedNodes":[20]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":3,"y":5},{"x":4,"y":5},{"x":3,"y":4}],"type":"BROWN"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":6,"y":1},{"x":6,"y":2},{"x":6,"y":3}],"type":"BROWN"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":5,"y":2},{"x":4,"y":2}],"type":"BROWN"}]',
        destinations='[[8,3]]',
        origin='{"coordinate":[0,6],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution=[11],
    )
    level111.save()
    set_decor(level111, json.loads('[{"x":708,"y":477,"z":2,"decorName":"pond"},{"x":590,"y":567,"z":3,"decorName":"bush"},{"x":467,"y":631,"z":3,"decorName":"bush"},{"x":124,"y":305,"z":4,"decorName":"tree1"},{"x":36,"y":396,"z":4,"decorName":"tree1"},{"x":95,"y":500,"z":4,"decorName":"tree1"}]'))
    set_blocks(level111, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"controls_repeat_until"},{"type":"at_destination"},{"type":"declare_event"},{"type":"puff_up"},{"type":"sound_horn"}]'))

    level112 = Level(
        name='112',
        episode=episode12,
        default=True,
        path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3,13]},{"coordinate":[2,5],"connectedNodes":[4,2]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7,15]},{"coordinate":[5,4],"connectedNodes":[6,8,16]},{"coordinate":[5,5],"connectedNodes":[9,7]},{"coordinate":[6,5],"connectedNodes":[8,10]},{"coordinate":[7,5],"connectedNodes":[9,11]},{"coordinate":[7,4],"connectedNodes":[10,12,18]},{"coordinate":[8,4],"connectedNodes":[11]},{"coordinate":[2,3],"connectedNodes":[2,14]},{"coordinate":[3,3],"connectedNodes":[13,15]},{"coordinate":[4,3],"connectedNodes":[14,6]},{"coordinate":[5,3],"connectedNodes":[7,17]},{"coordinate":[6,3],"connectedNodes":[16,18]},{"coordinate":[7,3],"connectedNodes":[17,11]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":4,"y":5},{"x":3,"y":5}],"type":"WHITE"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":6,"y":3},{"x":7,"y":3}],"type":"WHITE"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":4,"y":3},{"x":3,"y":3}],"type":"BROWN"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":7,"y":5},{"x":6,"y":5}],"type":"BROWN"}]',
        destinations='[[8,4]]',
        origin='{"coordinate":[0,4],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution=[11],
    )
    level112.save()
    set_decor(level112, json.loads('[{"x":451,"y":136,"z":2,"decorName":"pond"},{"x":612,"y":389,"z":4,"decorName":"tree1"},{"x":312,"y":389,"z":4,"decorName":"tree1"},{"x":499,"y":200,"z":4,"decorName":"tree2"},{"x":444,"y":201,"z":4,"decorName":"tree2"},{"x":389,"y":245,"z":4,"decorName":"tree2"},{"x":336,"y":200,"z":4,"decorName":"tree2"},{"x":539,"y":243,"z":4,"decorName":"tree2"},{"x":598,"y":198,"z":4,"decorName":"tree2"}]'))
    set_blocks(level112, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"declare_event"},{"type":"puff_up"},{"type":"sound_horn"}]'))

    level113 = Level(
        name='113',
        default=True,
        episode=episode12,
        path='[{"coordinate":[4,2],"connectedNodes":[1]},{"coordinate":[4,1],"connectedNodes":[2,0,13]},{"coordinate":[3,1],"connectedNodes":[3,1]},{"coordinate":[2,1],"connectedNodes":[4,2]},{"coordinate":[1,1],"connectedNodes":[5,3]},{"coordinate":[1,2],"connectedNodes":[6,4]},{"coordinate":[1,3],"connectedNodes":[7,5]},{"coordinate":[1,4],"connectedNodes":[8,6]},{"coordinate":[2,4],"connectedNodes":[7,9]},{"coordinate":[3,4],"connectedNodes":[8,11]},{"coordinate":[4,6],"connectedNodes":[18,12]},{"coordinate":[4,4],"connectedNodes":[9,12]},{"coordinate":[4,5],"connectedNodes":[10,11]},{"coordinate":[5,1],"connectedNodes":[1,14]},{"coordinate":[6,1],"connectedNodes":[13,15]},{"coordinate":[7,1],"connectedNodes":[14,16]},{"coordinate":[8,1],"connectedNodes":[15,26]},{"coordinate":[6,6],"connectedNodes":[18,19]},{"coordinate":[5,6],"connectedNodes":[10,17]},{"coordinate":[7,6],"connectedNodes":[17,20]},{"coordinate":[8,6],"connectedNodes":[19,21]},{"coordinate":[9,6],"connectedNodes":[20,22]},{"coordinate":[9,5],"connectedNodes":[21,23]},{"coordinate":[9,4],"connectedNodes":[22,24]},{"coordinate":[9,3],"connectedNodes":[23,25]},{"coordinate":[9,2],"connectedNodes":[24,26]},{"coordinate":[9,1],"connectedNodes":[16,25]}]',
        traffic_lights='[]',
        cows='[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":9,"y":1},{"x":8,"y":1},{"x":9,"y":2}],"type":"WHITE"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":6,"y":6},{"x":5,"y":6},{"x":7,"y":6}],"type":"WHITE"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":1,"y":3},{"x":3,"y":4},{"x":2,"y":4}],"type":"BROWN"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":1,"y":2},{"x":1,"y":1}],"type":"BROWN"},{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":9,"y":6},{"x":9,"y":4}],"type":"WHITE"}]',
        destinations='[[4,5]]',
        origin='{"coordinate":[4,2],"direction":"S"}',
        max_fuel=15,
        blocklyEnabled=True,
        pythonEnabled=False,
        disable_route_score=True,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id='1'),
        model_solution=[7],
    )
    level113.save()
    set_decor(level113, json.loads('[{"x":231,"y":249,"z":2,"decorName":"pond"},{"x":799,"y":338,"z":4,"decorName":"tree2"},{"x":556,"y":360,"z":4,"decorName":"tree2"},{"x":680,"y":278,"z":4,"decorName":"tree1"},{"x":758,"y":462,"z":4,"decorName":"tree1"},{"x":621,"y":479,"z":4,"decorName":"tree1"}]'))
    set_blocks(level113, json.loads('[{"type":"move_forwards"},{"type":"turn_left"},{"type":"turn_right"},{"type":"controls_repeat"},{"type":"controls_repeat_until"},{"type":"at_destination"},{"type":"declare_event"},{"type":"puff_up"},{"type":"sound_horn"}]'))

    level110.next_level = level111
    level111.next_level = level112
    level112.next_level = level113

    level110.save()
    level111.save()
    level112.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0050_level_score_40'),
    ]

    operations = [
        migrations.RunPython(add_levels),
    ]
