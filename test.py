from abilities_folder.hero_all_ponts import points_for_abilities,ability_picked_count
import abilities_folder.hero_all_ponts
def test():
    abilities_folder.hero_all_ponts.ability_picked_count+=1
    print(points_for_abilities)
    print(abilities_folder.hero_all_ponts.ability_picked_count)

test()
