import json

mat_names = [('dragonbone', 'dragon'), ('fire_dragonbone', 'fire_dragon'), ('ice_dragonbone', 'ice_dragon'),
    ('desert', 'desert'), ('desert_venom', 'desert_venom'), ('jungle', 'jungle'),
    ('jungle_venom', 'jungle_venom'), ('fire_dragonsteel', 'dragonsteel_fire'),
    ('ice_dragonsteel', 'dragonsteel_ice')]

def gen_simple_item_model(mat_name, weapon_name, mod_name, texture_name):
    gen_dict = {
        "parent":"spartanweaponry:item/" + weapon_name + "_wood",
        "textures": {
            "layer0": mod_name + ":items/" + weapon_name + "_" + texture_name
        }
    }
    with open(weapon_name + '_' + mat_name + '.json', 'w') as outfile:
        json.dump(gen_dict, outfile) 

def gen_quarterstaff_model(mat_name, weapon_name, mod_name, texture_name):
    gen_dict = {
        "parent":"spartanweaponry:item/staff",
        "textures": {
            "layer0": mod_name + ":items/" + "quarter" + weapon_name + "_" + texture_name
        }
    }
    with open(weapon_name + '_' + mat_name + '.json', 'w') as outfile:
        json.dump(gen_dict, outfile) 


def gen_pulling(mat_name, weapon_name, mod_name, texture_name, pull_count, base_pull):
    gen_dict = {
        "parent":"spartanweaponry:item/" + weapon_name + "_wood_pulling_" + base_pull,
        "textures": {
            "layer0": mod_name + ":items/" + weapon_name + "_" + texture_name + "_pulling_" + pull_count
        }
    }
    with open(weapon_name + '_' + mat_name + "_pulling_" + pull_count + '.json', 'w') as outfile:
        json.dump(gen_dict, outfile)

def gen_firing(mat_name, weapon_name, mod_name, texture_name):
    gen_dict = {
        "parent": "spartanweaponry:item/" + weapon_name + "_wood_pulling_0",
        "textures": {
            "layer0": mod_name + ":items/" + weapon_name + "_" + texture_name + "_loaded"
        }
    }
    with open(weapon_name + '_' + mat_name + '_firing.json', 'w') as outfile:
        json.dump(gen_dict, outfile)


def gen_loaded(mat_name, weapon_name, mod_name, texture_name):
    gen_dict = {
        "parent": "spartanweaponry:item/" + weapon_name + "_wood",
        "textures": {
            "layer0": mod_name + ":items/" + weapon_name + "_" + texture_name + "_loaded"
        }
    }
    with open(weapon_name + '_' + mat_name + '_loaded.json', 'w') as outfile:
        json.dump(gen_dict, outfile)


def gen_crossbow(mat_name, mod_name, texture_name):
    gen_pulling(mat_name, "crossbow", mod_name, texture_name, "0", "0")
    gen_pulling(mat_name, "crossbow", mod_name, texture_name, "1", "0")
    gen_pulling(mat_name, "crossbow", mod_name, texture_name, "2", "0")
    gen_firing(mat_name, "crossbow", mod_name, texture_name)
    gen_loaded(mat_name, "crossbow", mod_name, texture_name)
    gen_dict = {
        "parent": "spartanweaponry:item/crossbow_wood",
        "textures": {
            "layer0": mod_name + ":items/crossbow_" + texture_name + "_standby"
        },
        "overrides": [
            {
                "predicate": {
                    "pulling": 1
                },
                "model": mod_name + ":item/crossbow_" + mat_name + "_pulling_0"
            },
            {
                "predicate": {
                    "pulling": 1,
                    "pull": 0.65
                },
                "model": mod_name + ":item/crossbow_" + mat_name + "_pulling_1"
            },
            {
                "predicate": {
                    "pulling": 1,
                    "pull": 0.9
                },
                "model": mod_name + ":item/crossbow_" + mat_name + "_pulling_2"
            },
            {
                "predicate": {
                    "pulling": 0,
                    "pull": 1.0
                },
                "model": mod_name + ":item/crossbow_" + mat_name + "_loaded"
            },
            {
                "predicate": {
                    "pulling": 1,
                    "pull": 1.0
                },
                "model": mod_name + ":item/crossbow_" + mat_name + "_firing"
            }
      ]
    }
    with open('crossbow_' + mat_name + '.json', 'w') as outfile:
        json.dump(gen_dict, outfile)


def gen_longbow(mat_name, mod_name, texture_name):
    gen_pulling(mat_name, "longbow", mod_name, texture_name, "0", "0")
    gen_pulling(mat_name, "longbow", mod_name, texture_name, "1", "1")
    gen_pulling(mat_name, "longbow", mod_name, texture_name, "2", "2")
    gen_dict = {
    "parent": "spartanweaponry:item/longbow_wood",
        "textures": {
            "layer0": mod_name + ":items/longbow_" + texture_name + "_standby"
        },
        "overrides": [
            {
              "predicate": {
                "pulling": 1
              },
              "model": mod_name + ":item/longbow_" + mat_name + "_pulling_0"
            },
            {
              "predicate": {
                "pulling": 1,
                "pull": 0.65
              },
              "model": mod_name + ":item/longbow_" + mat_name + "_pulling_1"
            },
            {
              "predicate": {
                "pulling": 1,
                "pull": 0.9
              },
              "model": mod_name + ":item/longbow_" + mat_name + "_pulling_2"
            }
        ]
    }
    with open('longbow_' + mat_name + '.json', 'w') as outfile:
        json.dump(gen_dict, outfile)


MOD_NAME = "saf2021"

for mat_name, texture_name in mat_names:
    gen_simple_item_model(mat_name, "katana", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "boomerang", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "dagger", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "greatsword", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "halberd", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "hammer", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "javelin", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "lance", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "longsword", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "mace", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "pike", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "rapier", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "saber", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "spear", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "throwing_axe", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "throwing_knife", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "warhammer", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "battleaxe", MOD_NAME, texture_name)
    gen_quarterstaff_model(mat_name, "staff", MOD_NAME, texture_name)
    gen_simple_item_model(mat_name, "glaive", MOD_NAME, texture_name)
    gen_longbow(mat_name, MOD_NAME, texture_name)
    gen_crossbow(mat_name, MOD_NAME, texture_name)
  
