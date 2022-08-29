#! /usr/bin/env python3

eggs = {
    "axolotl_spawn_egg": "axolotl_bucket", # 美西螈刷怪蛋
    "bat_spawn_egg": "", # 蝙蝠刷怪蛋
    "bee_spawn_egg": "honey_bottle", # 蜜蜂刷怪蛋
    "blaze_spawn_egg": "blaze_rod", # 烈焰人刷怪蛋
    "cave_spider_spawn_egg": "cobweb", # 洞穴蜘蛛刷怪蛋
    "cat_spawn_egg": "", # 猫刷怪蛋
    "chicken_spawn_egg": "chicken", # 鸡刷怪蛋
    "cod_spawn_egg": "cod", # 鳕鱼刷怪蛋
    "cow_spawn_egg": "beef", # 牛刷怪蛋
    "creeper_spawn_egg": "gunpowder", # 苦力怕刷怪蛋
    "dolphin_spawn_egg": "", # 海豚刷怪蛋
    "donkey_spawn_egg": "", # 驴刷怪蛋
    "drowned_spawn_egg": "", # 溺尸刷怪蛋
    "elder_guardian_spawn_egg": "", # 远古守卫者刷怪蛋
    "enderman_spawn_egg": "ender_pearl", # 末影人刷怪蛋
    "endermite_spawn_egg": "", # 末影螨刷怪蛋
    "evoker_spawn_egg": "", # 唤魔者刷怪蛋
    "fox_spawn_egg": "", # 狐狸刷怪蛋
    "frog_spawn_egg": "", # 青蛙刷怪蛋
    "ghast_spawn_egg": "ghast_tear", # 恶魂刷怪蛋
    "glow_squid_spawn_egg": "glow_ink_sac", # 发光鱿鱼刷怪蛋
    "goat_spawn_egg": "goat_horn", # 山羊刷怪蛋
    "guardian_spawn_egg": "", # 守卫者刷怪蛋
    "hoglin_spawn_egg": "", # 疣猪兽刷怪蛋
    "horse_spawn_egg": "", # 马刷怪蛋
    "husk_spawn_egg": "", # 尸壳刷怪蛋
    "llama_spawn_egg": "", # 羊驼刷怪蛋
    "magma_cube_spawn_egg": "magma_cream", # 岩浆怪刷怪蛋
    "mooshroom_spawn_egg": "", # 哞菇刷怪蛋
    "mule_spawn_egg": "", # 骡刷怪蛋
    "ocelot_spawn_egg": "", # 豹猫刷怪蛋
    "panda_spawn_egg": "", # 熊猫刷怪蛋
    "parrot_spawn_egg": "", # 鹦鹉刷怪蛋
    "phantom_spawn_egg": "phantom_membrane", # 幻翼刷怪蛋
    "pig_spawn_egg": "porkchop", # 猪刷怪蛋
    "piglin_spawn_egg": "", # 猪灵刷怪蛋
    "piglin_brute_spawn_egg": "", # 猪灵蛮兵刷怪蛋
    "polar_bear_spawn_egg": "", # 北极熊刷怪蛋
    "pufferfish_spawn_egg": "pufferfish_bucket", # 河豚刷怪蛋
    "rabbit_spawn_egg": "rabbit", # 兔子刷怪蛋
    "ravager_spawn_egg": "", # 劫掠兽刷怪蛋
    "salmon_spawn_egg": "salmon_bucket", # 鲑鱼刷怪蛋
    "sheep_spawn_egg": "mutton", # 绵羊刷怪蛋
    "shulker_spawn_egg": "shulker_shell", # 潜影贝刷怪蛋
    "silverfish_spawn_egg": "", # 蠹虫刷怪蛋
    "skeleton_spawn_egg": "bone", # 骷髅刷怪蛋
    "skeleton_horse_spawn_egg": "", # 骷髅马刷怪蛋
    "slime_spawn_egg": "slime_ball", # 史莱姆刷怪蛋
    "spider_spawn_egg": "spider_eye", # 蜘蛛刷怪蛋
    "squid_spawn_egg": "ink_sac", # 鱿鱼刷怪蛋
    "stray_spawn_egg": "", # 流浪者刷怪蛋
    "strider_spawn_egg": "", # 炽足兽刷怪蛋
    "tadpole_spawn_egg": "tadpole_bucket", # 蝌蚪刷怪蛋
    "trader_llama_spawn_egg": "", # 行商羊驼刷怪蛋
    "tropical_fish_spawn_egg": "tropical_fish_bucket", # 热带鱼刷怪蛋
    "turtle_spawn_egg": "scute", # 海龟刷怪蛋
    "vex_spawn_egg": "", # 恼鬼刷怪蛋
    "villager_spawn_egg": "", # 村民刷怪蛋
    "vindicator_spawn_egg": "", # 卫道士刷怪蛋
    "wandering_trader_spawn_egg": "", # 流浪商人刷怪蛋
    "warden_spawn_egg": "", # 监守者刷怪蛋
    "witch_spawn_egg": "", # 女巫刷怪蛋
    "wither_skeleton_spawn_egg": "wither_skeleton_skull", # 凋灵骷髅刷怪蛋
    "wolf_spawn_egg": "", # 狼刷怪蛋
    "zombie_spawn_egg": "rotten_flesh", # 僵尸刷怪蛋
    "zombie_horse_spawn_egg": "", # 僵尸马刷怪蛋
    "zombie_villager_spawn_egg": "", # 僵尸村民刷怪蛋
    "zombified_piglin_spawn_egg": "", # 僵尸猪灵刷怪蛋
}

for target in eggs:
    item:str = eggs[target]
    if item == '':
        continue
    with open(f'data/spawn/recipes/{target}.json', "w") as file:
        file.write(f'''{{
    "type": "minecraft:crafting_shaped",
    "pattern": [
        "BBB",
        "DAE",
        "CCC"
    ],
    "key": {{
        "A": {{
            "item": "minecraft:egg"
        }},
        "B": {{
            "item": "minecraft:warped_fungus"
        }},
        "C": {{
            "item": "minecraft:crimson_fungus"
        }},
        "D": {{
            "item": "minecraft:dragon_breath"
        }},
        "E": {{
            "item": "minecraft:{item}"
        }}
    }},
    "result": {{
        "item": "minecraft:{target}",
        "count": 1
    }}
}}
''')