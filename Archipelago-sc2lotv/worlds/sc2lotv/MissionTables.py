from typing import NamedTuple, Dict, List
from enum import IntEnum

# no_build_regions_list = ["Liberation Day", "Breakout", "Ghost of a Chance", "Piercing the Shroud", "Whispers of Doom",
#                          "Belly of the Beast"]
# easy_regions_list = ["The Outlaws", "Zero Hour", "Evacuation", "Outbreak", "Smash and Grab", "Devil's Playground"]
# medium_regions_list = ["Safe Haven", "Haven's Fall", "The Dig", "The Moebius Factor", "Supernova",
#                        "Welcome to the Jungle", "The Great Train Robbery", "Cutthroat", "Media Blitz",
#                        "A Sinister Turn", "Echoes of the Future"]
# hard_regions_list = ["Maw of the Void", "Engine of Destruction", "In Utter Darkness", "Gates of Hell",
#                      "Shatter the Sky"]

no_build_regions_list = ["Evil Awoken", "For Aiur!", "The Infinite Cycle", "Templar(s) Return"]
starter_regions_list = ["Dark Whispers", "The Growing Shadow", "The Spear of Adun"]
easy_regions_list = ["Sky Shield", "Amon(s) Reach", "Brothers in Arms", "Last Stand"]
medium_regions_list = ["Ghosts in the Fog", "Forbidden Weapon", "Temple of Unification", "Harbinger of Oblivion",
                       "Unsealing the Past", "Steps of the Rite"]
hard_regions_list = ["Purification", "Rak Shir", "Templar(s) Charge", "The Host"]


class MissionPools(IntEnum):
    STARTER = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3
    FINAL = 4


class MissionInfo(NamedTuple):
    id: int
    required_world: List[int]
    category: str
    number: int = 0  # number of worlds need beaten
    completion_critical: bool = False  # missions needed to beat game
    or_requirements: bool = False  # true if the requirements should be or-ed instead of and-ed


class FillMission(NamedTuple):
    type: int
    connect_to: List[int]  # -1 connects to Menu
    category: str
    number: int = 0  # number of worlds need beaten
    completion_critical: bool = False  # missions needed to beat game
    or_requirements: bool = False  # true if the requirements should be or-ed instead of and-ed
    removal_priority: int = 0  # how many missions missing from the pool required to remove this mission


vanilla_shuffle_order = [
    FillMission(MissionPools.EASY, [-3], "Prologue", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [-2], "Prologue", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [-1], "Prologue", completion_critical=True, removal_priority=1),
    FillMission(MissionPools.STARTER, [0], "Aiur", completion_critical=True),
    FillMission(MissionPools.EASY, [1], "Aiur", completion_critical=True),
    FillMission(MissionPools.EASY, [2], "Aiur", completion_critical=True, removal_priority=2),
    FillMission(MissionPools.EASY, [6], "Korhal", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [7], "Korhal", completion_critical=True, removal_priority=3),
    FillMission(MissionPools.EASY, [6], "Shakuras", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [9], "Shakuras", completion_critical=True, removal_priority=4),
    FillMission(MissionPools.MEDIUM, [8, 10], "Purifier", completion_critical=True, or_requirements=True),
    FillMission(MissionPools.MEDIUM, [8, 10, 11], "Ulnar", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [12], "Ulnar", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [13], "Ulnar", completion_critical=True, removal_priority=5),
    FillMission(MissionPools.MEDIUM, [14], "Purifier", completion_critical=True),
    FillMission(MissionPools.HARD, [15], "Purifier", completion_critical=True, removal_priority=6),
    FillMission(MissionPools.MEDIUM, [14], "Taldarim", completion_critical=True),
    FillMission(MissionPools.HARD, [17], "Taldarim", completion_critical=True, removal_priority=7),
    FillMission(MissionPools.HARD, [16, 18], "Moebius", completion_critical=True, or_requirements=True),
    FillMission(MissionPools.HARD, [16, 18, 19], "Aiur Revisit", completion_critical=True),
    FillMission(MissionPools.HARD, [20], "Aiur Revisit", completion_critical=True),
    FillMission(MissionPools.FINAL, [21], "Aiur Revisit", completion_critical=True),

    #    FillMission(MissionPools.STARTER, [-1], "Umoja", completion_critical=True),
    #    FillMission(MissionPools.EASY, [0], "Umoja", completion_critical=True),
    #    FillMission(MissionPools.EASY, [1], "Umoja", completion_critical=True, removal_priority=1),
    #    FillMission(MissionPools.EASY, [2], "Kaldir", completion_critical=True),
    #    FillMission(MissionPools.MEDIUM, [3], "Kaldir", completion_critical=True, removal_priority=2),
    #    FillMission(MissionPools.MEDIUM, [4], "Kaldir", completion_critical=True),
    #    FillMission(MissionPools.EASY, [2], "Char", completion_critical=True),
    #    FillMission(MissionPools.MEDIUM, [6], "Char", completion_critical=True, removal_priority=3),
    #    FillMission(MissionPools.MEDIUM, [7], "Char", completion_critical=True),
    #    FillMission(MissionPools.MEDIUM, [5,8], "Zerus", completion_critical=True, or_requirements=True),
    #    FillMission(MissionPools.MEDIUM, [9], "Zerus", completion_critical=True, removal_priority=4),
    #    FillMission(MissionPools.MEDIUM, [10], "Zerus", completion_critical=True),
    #    FillMission(MissionPools.MEDIUM, [5, 8, 11], "Skygeirr Station", completion_critical=True),
    #    FillMission(MissionPools.HARD, [12], "Skygeirr Station", completion_critical=True, removal_priority=5),
    #    FillMission(MissionPools.HARD, [13], "Skygeirr Station", completion_critical=True),
    #    FillMission(MissionPools.MEDIUM, [5, 8, 11], "Dominion Space", completion_critical=True),
    #    FillMission(MissionPools.HARD, [15], "Dominion Space", completion_critical=True),
    #    FillMission(MissionPools.HARD, [14,16], "Korhal", completion_critical=True),
    #    FillMission(MissionPools.HARD, [17], "Korhal", completion_critical=True),
    #    FillMission(MissionPools.FINAL, [18], "Korhal", completion_critical=True),

    # FillMission(MissionPools.STARTER, [-1], "Mar Sara", completion_critical=True),
    # FillMission(MissionPools.EASY, [0], "Mar Sara", completion_critical=True),
    # FillMission(MissionPools.EASY, [1], "Mar Sara", completion_critical=True),
    # FillMission(MissionPools.EASY, [2], "Colonist"),
    # FillMission(MissionPools.MEDIUM, [3], "Colonist"),
    # FillMission(MissionPools.HARD, [4], "Colonist", number=7),
    # FillMission(MissionPools.HARD, [4], "Colonist", number=7, removal_priority=1),
    # FillMission(MissionPools.EASY, [2], "Artifact", completion_critical=True),
    # FillMission(MissionPools.MEDIUM, [7], "Artifact", number=8, completion_critical=True),
    # FillMission(MissionPools.HARD, [8], "Artifact", number=11, completion_critical=True),
    # FillMission(MissionPools.HARD, [9], "Artifact", number=14, completion_critical=True),
    # FillMission(MissionPools.HARD, [10], "Artifact", completion_critical=True),
    # FillMission(MissionPools.MEDIUM, [2], "Covert", number=4),
    # FillMission(MissionPools.MEDIUM, [12], "Covert"),
    # FillMission(MissionPools.HARD, [13], "Covert", number=8, removal_priority=3),
    # FillMission(MissionPools.HARD, [13], "Covert", number=8, removal_priority=2),
    # FillMission(MissionPools.MEDIUM, [2], "Rebellion", number=6),
    # FillMission(MissionPools.HARD, [16], "Rebellion"),
    # FillMission(MissionPools.HARD, [17], "Rebellion"),
    # FillMission(MissionPools.HARD, [18], "Rebellion"),
    # FillMission(MissionPools.HARD, [19], "Rebellion", removal_priority=5),
    # FillMission(MissionPools.MEDIUM, [8], "Prophecy", removal_priority=9),
    # FillMission(MissionPools.HARD, [21], "Prophecy", removal_priority=8),
    # FillMission(MissionPools.HARD, [22], "Prophecy", removal_priority=7),
    # FillMission(MissionPools.HARD, [23], "Prophecy", removal_priority=6),
    # FillMission(MissionPools.HARD, [11], "Char", completion_critical=True),
    # FillMission(MissionPools.HARD, [25], "Char", completion_critical=True, removal_priority=4),
    # FillMission(MissionPools.HARD, [25], "Char", completion_critical=True),
    # FillMission(MissionPools.FINAL, [26, 27], "Char", completion_critical=True, or_requirements=True)
]

mini_campaign_order = [

FillMission(MissionPools.STARTER, [-1], "Prologue", completion_critical=True),
    FillMission(MissionPools.EASY, [0], "Aiur"),
    FillMission(MissionPools.EASY, [1], "Aiur"),
    FillMission(MissionPools.EASY, [2], "Korhal"),
    FillMission(MissionPools.MEDIUM, [4], "Shakuras"),
    FillMission(MissionPools.MEDIUM, [3, 5], "Purifier", number=3, or_requirements=True),
    FillMission(MissionPools.MEDIUM, [3, 5, 6], "Ulnar"),
    FillMission(MissionPools.MEDIUM, [7], "Ulnar", number=5),
    FillMission(MissionPools.HARD, [8], "Purifer"),
    FillMission(MissionPools.HARD, [10], "Taldarim", number=5),
    FillMission(MissionPools.HARD, [9, 11], "Moebius", or_requirements=True),
    FillMission(MissionPools.HARD, [9, 11, 12], "Aiur Revisit", completion_critical=True, number=8),
    FillMission(MissionPools.FINAL, [13], "Aiur Revisit", completion_critical=True),


    #FillMission(MissionPools.STARTER, [-1], "Umoja", completion_critical=True),
    #FillMission(MissionPools.EASY, [0], "Kaldir"),
    #FillMission(MissionPools.MEDIUM, [1], "Kaldir"),
    #FillMission(MissionPools.EASY, [0], "Char"),
    #FillMission(MissionPools.MEDIUM, [3], "Char"),
    #FillMission(MissionPools.MEDIUM, [0], "Zerus", number=3),
    #FillMission(MissionPools.MEDIUM, [5], "Zerus"),
    #FillMission(MissionPools.HARD, [6], "Skygeirr Station", number=5),
    #FillMission(MissionPools.HARD, [7], "Skygeirr Station"),
    #FillMission(MissionPools.HARD, [6], "Dominion Space", number=5),
    #FillMission(MissionPools.HARD, [9], "Dominion Space"),
    #FillMission(MissionPools.HARD, [5], "Korhal", completion_critical=True, number=8),
    #FillMission(MissionPools.FINAL, [11], "Korhal", completion_critical=True),

    # FillMission(MissionPools.STARTER, [-1], "Mar Sara", completion_critical=True),
    # FillMission(MissionPools.EASY, [0], "Colonist"),
    # FillMission(MissionPools.MEDIUM, [1], "Colonist"),
    # FillMission(MissionPools.EASY, [0], "Artifact", completion_critical=True),
    # FillMission(MissionPools.MEDIUM, [3], "Artifact", number=4, completion_critical=True),
    # FillMission(MissionPools.HARD, [4], "Artifact", number=8, completion_critical=True),
    # FillMission(MissionPools.MEDIUM, [0], "Covert", number=2),
    # FillMission(MissionPools.HARD, [6], "Covert"),
    # FillMission(MissionPools.MEDIUM, [0], "Rebellion", number=3),
    # FillMission(MissionPools.HARD, [8], "Rebellion"),
    # FillMission(MissionPools.MEDIUM, [4], "Prophecy"),
    # FillMission(MissionPools.HARD, [10], "Prophecy"),
    # FillMission(MissionPools.HARD, [5], "Char", completion_critical=True),
    # FillMission(MissionPools.HARD, [5], "Char", completion_critical=True),
    # FillMission(MissionPools.FINAL, [12, 13], "Char", completion_critical=True, or_requirements=True)
]

gauntlet_order = [
    FillMission(MissionPools.STARTER, [-1], "I", completion_critical=True),
    FillMission(MissionPools.EASY, [0], "II", completion_critical=True),
    FillMission(MissionPools.EASY, [1], "III", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [2], "IV", completion_critical=True),
    FillMission(MissionPools.MEDIUM, [3], "V", completion_critical=True),
    FillMission(MissionPools.HARD, [4], "VI", completion_critical=True),
    FillMission(MissionPools.FINAL, [5], "Final", completion_critical=True)
]

grid_order = [
    FillMission(MissionPools.STARTER, [-1], "_1"),
    FillMission(MissionPools.EASY, [0], "_1"),
    FillMission(MissionPools.MEDIUM, [1, 6, 3], "_1", or_requirements=True),
    FillMission(MissionPools.HARD, [2, 7], "_1", or_requirements=True, removal_priority=1),
    FillMission(MissionPools.EASY, [0], "_2"),
    FillMission(MissionPools.MEDIUM, [1, 4], "_2", or_requirements=True),
    FillMission(MissionPools.HARD, [2, 5, 10, 7], "_2", or_requirements=True),
    FillMission(MissionPools.HARD, [3, 6, 11], "_2", or_requirements=True, removal_priority=2),
    FillMission(MissionPools.MEDIUM, [4, 9, 12], "_3", or_requirements=True),
    FillMission(MissionPools.HARD, [5, 8, 10, 13], "_3", or_requirements=True),
    FillMission(MissionPools.HARD, [6, 9, 11, 14], "_3", or_requirements=True),
    FillMission(MissionPools.HARD, [7, 10], "_3", or_requirements=True, removal_priority=3),
    FillMission(MissionPools.HARD, [8, 13], "_4", or_requirements=True),
    FillMission(MissionPools.HARD, [9, 12, 14], "_4", or_requirements=True),
    FillMission(MissionPools.HARD, [10, 13], "_4", or_requirements=True),
    FillMission(MissionPools.FINAL, [11, 14], "_4", or_requirements=True)
]

mini_grid_order = [
    FillMission(MissionPools.STARTER, [-1], "_1"),
    FillMission(MissionPools.EASY, [0], "_1"),
    FillMission(MissionPools.MEDIUM, [1, 5], "_1", or_requirements=True),
    FillMission(MissionPools.EASY, [0], "_2"),
    FillMission(MissionPools.MEDIUM, [1, 3], "_2", or_requirements=True),
    FillMission(MissionPools.HARD, [2, 4], "_2", or_requirements=True),
    FillMission(MissionPools.MEDIUM, [3, 7], "_3", or_requirements=True),
    FillMission(MissionPools.HARD, [4, 6], "_3", or_requirements=True),
    FillMission(MissionPools.FINAL, [5, 7], "_3", or_requirements=True)
]

blitz_order = [
    FillMission(MissionPools.STARTER, [-1], "I"),
    FillMission(MissionPools.EASY, [-1], "I"),
    FillMission(MissionPools.MEDIUM, [0, 1], "II", number=1, or_requirements=True),
    FillMission(MissionPools.MEDIUM, [0, 1], "II", number=1, or_requirements=True),
    FillMission(MissionPools.MEDIUM, [0, 1], "III", number=2, or_requirements=True),
    FillMission(MissionPools.MEDIUM, [0, 1], "III", number=2, or_requirements=True),
    FillMission(MissionPools.HARD, [0, 1], "IV", number=3, or_requirements=True),
    FillMission(MissionPools.HARD, [0, 1], "IV", number=3, or_requirements=True),
    FillMission(MissionPools.HARD, [0, 1], "V", number=4, or_requirements=True),
    FillMission(MissionPools.HARD, [0, 1], "V", number=4, or_requirements=True),
    FillMission(MissionPools.HARD, [0, 1], "Final", number=5, or_requirements=True),
    FillMission(MissionPools.FINAL, [0, 1], "Final", number=5, or_requirements=True)
]

mission_orders = [vanilla_shuffle_order, vanilla_shuffle_order, mini_campaign_order, grid_order, mini_grid_order,
                  blitz_order, gauntlet_order]

vanilla_mission_req_table = {

    "Dark Whispers": MissionInfo(1, [], "Prologue", completion_critical=True),
    "Ghosts in the Fog": MissionInfo(2, [1], "Prologue", completion_critical=True),
    "Evil Awoken": MissionInfo(3, [2], "Prologue", completion_critical=True),
    "For Aiur!": MissionInfo(4, [], "Aiur", completion_critical=True),
    "The Growing Shadow": MissionInfo(5, [4], "Aiur", completion_critical=True),
    "The Spear of Adun": MissionInfo(6, [5], "Aiur", completion_critical=True),
    "Sky Shield": MissionInfo(7, [6], "Korhal", completion_critical=True),
    "Brothers in Arms": MissionInfo(8, [7], "Korhal", completion_critical=True),
    "Amon(s) Reach": MissionInfo(9, [6], "Shakuras", completion_critical=True),
    "Last Stand": MissionInfo(10, [9], "Shakuras", completion_critical=True),
    "Forbidden Weapon": MissionInfo(11, [8, 10], "Purifier", completion_critical=True, or_requirements=True),
    "Temple of Unification": MissionInfo(12, [11], "Ulnar", completion_critical=True),
    "The Infinite Cycle": MissionInfo(13, [12], "Ulnar", completion_critical=True),  #should have and requirement 8,10,11
    "Harbinger of Oblivion": MissionInfo(14, [13], "Ulnar", completion_critical=True),
    "Unsealing the Past": MissionInfo(15, [14], "Purifier", completion_critical=True),
    "Purification": MissionInfo(16, [15], "Purifier", completion_critical=True),
    "Steps of the Rite": MissionInfo(17, [14], "Taldarim", completion_critical=True),
    "Rak Shir": MissionInfo(18, [17], "Taldarim", completion_critical=True),
    "Templar(s) Charge": MissionInfo(19, [16, 18], "Moebius", completion_critical=True, or_requirements=True),
    "Templar(s) Return": MissionInfo(20, [19], "Aiur Revisit", completion_critical=True), #should have and requirment 16,18,19
    "The Host": MissionInfo(21, [20], "Aiur Revisit", completion_critical=True),
    "Salvation": MissionInfo(22, [21], "Aiur Revisit", completion_critical=True),

    # "Lab Rat": MissionInfo(1, [], "Umoja", completion_critical=True),
    # "Back in the Saddle": MissionInfo(2, [1], "Umoja", completion_critical=True),
    # "Rendezvous": MissionInfo(3, [2], "Umoja", completion_critical=True),
    # "Harvest of Screams": MissionInfo(4, [3], "Kaldir", completion_critical=True),
    # "Shoot the Messenger": MissionInfo(5, [4], "Kaldir", completion_critical=True),
    # "Enemy Within": MissionInfo(6, [5], "Kaldir", completion_critical=True),
    # "Domination": MissionInfo(7, [3], "Char", completion_critical=True),
    # "Fire in the Sky": MissionInfo(8, [7], "Char", completion_critical=True),
    # "Old Soldiers": MissionInfo(9, [8], "Char", completion_critical=True),
    # "Waking the Ancient": MissionInfo(10, [6, 9], "Zerus", completion_critical=True, or_requirements=True),
    # "The Crucible": MissionInfo(11, [10], "Zerus", completion_critical=True),
    # "Supreme": MissionInfo(12, [11], "Zerus", completion_critical=True),
    # "Infested": MissionInfo(13, [12], "Skygeirr Station", completion_critical=True),
    # "Hand of Darkness": MissionInfo(14, [13], "Skygeirr Station", completion_critical=True),
    # "Phantoms of the Void": MissionInfo(15, [14], "Skygeirr Station", completion_critical=True),
    # "With Friends Like These": MissionInfo(16, [12], "Dominion Space", completion_critical=True),
    # "Conviction": MissionInfo(17, [16], "Dominion Space", completion_critical=True),
    # "Planetfall": MissionInfo(18, [15, 17], "Korhal", completion_critical=True),
    # "Death From Above": MissionInfo(19, [18], "Korhal", completion_critical=True),
    # "The Reckoning": MissionInfo(20, [19], "Korhal", completion_critical=True)
    # "Lab Rat": MissionInfo(1, [], "Umoja", completion_critical=True),
    # "Back in the Saddle": MissionInfo(2, [1], "Umoja", completion_critical=True),
    # "Rendezvous": MissionInfo(3, [2], "Umoja", completion_critical=True),
    # "Harvest of Screams": MissionInfo(4, [3], "Kaldir"),
    # "Shoot the Messenger": MissionInfo(5, [4], "Kaldir"),
    # "Enemy Within": MissionInfo(6, [5], "Kaldir"),
    # "Domination": MissionInfo(7, [3], "Char"),
    # "Fire in the Sky": MissionInfo(8, [7], "Char"),
    # "Old Soldiers": MissionInfo(9, [8], "Char"),
    # "Waking the Ancient": MissionInfo(10, [6, 9], "Zerus", completion_critical=True, or_requirements=True),
    # "The Crucible": MissionInfo(11, [10], "Zerus", completion_critical=True),
    # "Supreme": MissionInfo(12, [11], "Zerus", completion_critical=True),
    # "Infested": MissionInfo(13, [12], "Skygeirr Station", or_requirements=True),
    # should have and requirement (6, 9, 12)
    # "Hand of Darkness": MissionInfo(14, [13], "Skygeirr Station"),
    # "Phantoms of the Void": MissionInfo(15, [14], "Skygeirr Station"),
    # "With Friends Like These": MissionInfo(16, [12], "Dominion Space", or_requirements=True),
    # should have and requirement (6, 9, 12)
    # "Conviction": MissionInfo(17, [16], "Dominion Space"),
    # "Planetfall": MissionInfo(18, [15, 17], "Korhal", completion_critical=True),
    # "Death From Above": MissionInfo(19, [18], "Korhal", completion_critical=True),
    # "The Reckoning": MissionInfo(20, [19], "Korhal", completion_critical=True)

    # "Liberation Day": MissionInfo(1, [], "Mar Sara", completion_critical=True),
    # "The Outlaws": MissionInfo(2, [1], "Mar Sara", completion_critical=True),
    # "Zero Hour": MissionInfo(3, [2], "Mar Sara", completion_critical=True),
    # "Evacuation": MissionInfo(4, [3], "Colonist"),
    # "Outbreak": MissionInfo(5, [4], "Colonist"),
    # "Safe Haven": MissionInfo(6, [5], "Colonist", number=7),
    # "Haven's Fall": MissionInfo(7, [5], "Colonist", number=7),
    # "Smash and Grab": MissionInfo(8, [3], "Artifact", completion_critical=True),
    # "The Dig": MissionInfo(9, [8], "Artifact", number=8, completion_critical=True),
    # "The Moebius Factor": MissionInfo(10, [9], "Artifact", number=11, completion_critical=True),
    # "Supernova": MissionInfo(11, [10], "Artifact", number=14, completion_critical=True),
    # "Maw of the Void": MissionInfo(12, [11], "Artifact", completion_critical=True),
    # "Devil's Playground": MissionInfo(13, [3], "Covert", number=4),
    # "Welcome to the Jungle": MissionInfo(14, [13], "Covert"),
    # "Breakout": MissionInfo(15, [14], "Covert", number=8),
    # "Ghost of a Chance": MissionInfo(16, [14], "Covert", number=8),
    # "The Great Train Robbery": MissionInfo(17, [3], "Rebellion", number=6),
    # "Cutthroat": MissionInfo(18, [17], "Rebellion"),
    # "Engine of Destruction": MissionInfo(19, [18], "Rebellion"),
    # "Media Blitz": MissionInfo(20, [19], "Rebellion"),
    # "Piercing the Shroud": MissionInfo(21, [20], "Rebellion"),
    # "Whispers of Doom": MissionInfo(22, [9], "Prophecy"),
    # "A Sinister Turn": MissionInfo(23, [22], "Prophecy"),
    # "Echoes of the Future": MissionInfo(24, [23], "Prophecy"),
    # "In Utter Darkness": MissionInfo(25, [24], "Prophecy"),
    # "Gates of Hell": MissionInfo(26, [12], "Char", completion_critical=True),
    # "Belly of the Beast": MissionInfo(27, [26], "Char", completion_critical=True),
    # "Shatter the Sky": MissionInfo(28, [26], "Char", completion_critical=True),
    # "All-In": MissionInfo(29, [27, 28], "Char", completion_critical=True, or_requirements=True)
}

lookup_id_to_mission: Dict[int, str] = {
    data.id: mission_name for mission_name, data in vanilla_mission_req_table.items() if data.id}

starting_mission_locations = {

    "Dark Whispers": "Dark Whispers: Victory",
    "Evil Awoken": "Evil Awoken: Victory",
    "For Aiur!": "For Aiur! Victory",
    "The Infinite Cycle": "The Infinite Cycle: Victory",
    "Templar(s) Return": "Templar(s) Return: Victory",
    "The Growing Shadow": "The Growing Shadow: Victory",
    "The Spear of Adun": "The Spear of Adun: Victory",

    #"Lab Rat": "Lab Rat: Gather Minerals",
    #"Back in the Saddle": "Back in the Saddle: Victory",
    #"Harvest of Screams": "Harvest of Screams: First Ursadon Matriarch",
    #"Shoot the Messenger": "Shoot the Messenger: Center Stasis Chamber",
    #"Domination": "Domination: Repel Zagara",
    #"Fire in the Sky": "Fire in the Sky: West Biomass",
    #"Old Soldiers": "Old Soldiers: Get Nuked",
    #"Enemy Within": "Enemy Within: Victory",
    #"Waking the Ancient": "Waking the Ancient: Center Essence Pool",
    #"Supreme": "Supreme: Victory",
    #"With Friends Like These": "With Friends Like These: Victory",
    #"Conviction": "Conviction: Victory",

    # "Liberation Day": "Liberation Day: Victory",
    # "Breakout": "Breakout: Victory",
    # "Ghost of a Chance": "Ghost of a Chance: Victory",
    # "Piercing the Shroud": "Piercing the Shroud: Victory",
    # "Whispers of Doom": "Whispers of Doom: Victory",
    # "Belly of the Beast": "Belly of the Beast: Victory",
    # "Zero Hour": "Zero Hour: First Group Rescued",
    # "Evacuation": "Evacuation: First Chysalis",
    # "Devil's Playground": "Devil's Playground: Tosh's Miners",
    # "Smash and Grab": "Smash and Grab: First Relic",
    # "The Great Train Robbery": "The Great Train Robbery: North Defiler"
}

# alt_final_mission_locations = {
#     "Maw of the Void": "Maw of the Void: Victory",
#     "Engine of Destruction": "Engine of Destruction: Victory",
#     "Supernova": "Supernova: Victory",
#     "Gates of Hell": "Gates of Hell: Victory",
#     "Shatter the Sky": "Shatter the Sky: Victory"
# }
alt_final_mission_locations = {
    "The Host": "The Host: Victory",
    "Templar(s) Charge": "Templar(s) Charge: Victory",
    "Purification": "Purification: Victory",
    "Rak Shir": "Rak Shir: Vcitory"
}
