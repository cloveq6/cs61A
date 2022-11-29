# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing LongThrower miss
# ant = LongThrower()
# out_of_range = Bee(2)
# gamestate.places["tunnel_0_0"].add_insect(ant)
# gamestate.places["tunnel_0_4"].add_insect(out_of_range)
# ant.action(gamestate)
# print(out_of_range.armor)

# from ants import *
# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
# #
# # Testing fire does damage to all Bees in its Place
# place = gamestate.places['tunnel_0_4']
# fire = FireAnt(armor=1)
# place.add_insect(fire)        # Add a FireAnt with 1 armor
# place.add_insect(Bee(3))      # Add a Bee with 3 armor
# place.add_insect(Bee(5))      # Add a Bee with 5 armor
# print(len(place.bees))               # How many bees are there?

# place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
# print(fire.armor)
# print(fire.place is None)
# print(len(place.bees))
# print(place.bees[0].armor)

# class A:
#     fake = False
#     def __init__(self):
#         self.bb = A.fake
#         if A.fake == False:
#             A.fake = True


# class B(A):
#     pp = 1
        
        
# a = A()
# b = A()
# c = A()
# d = B()
# print(a.bb)    
# print(b.bb)   
# print(c.bb)
# print(isinstance(a, B))   

# class A:
#     aaa = 10

# a = A()
# A.aaa = 20
# b = A()
# c = A()

# print(a.aaa)    
# print(b.aaa)   
# print(c.aaa)

# a = None

# while a:
#     print("aa")


# test damage
# import ants, importlib
# importlib.reload(ants)
# beehive = ants.Hive(ants.AssaultPlan())
# dimensions = (2, 9)
# gamestate = ants.GameState(None, beehive, ants.ant_types(),
#         ants.dry_layout, dimensions)
# ants.bees_win = lambda: None
# # QueenAnt Placement
# queen = ants.QueenAnt()
# impostor = ants.QueenAnt()
# front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
# tunnel = [gamestate.places['tunnel_0_{0}'.format(i)]
#         for i in range(9)]
# tunnel[1].add_insect(back_ant)
# tunnel[7].add_insect(front_ant)
# tunnel[4].add_insect(impostor)
# impostor.action(gamestate)
# impostor.armor            # Impostors must die!
# tunnel[4].ant is None
# back_ant.damage           # Ants should not be buffed
# front_ant.damage
# tunnel[4].add_insect(queen)
# queen.action(gamestate)
# import ants, importlib
# importlib.reload(ants)
# beehive = ants.Hive(ants.AssaultPlan())
# dimensions = (2, 9)
# gamestate = ants.GameState(None, beehive, ants.ant_types(),
#         ants.dry_layout, dimensions)
# ants.bees_win = lambda: None
# # QueenAnt Placement
# queen = ants.QueenAnt()
# impostor = ants.QueenAnt()
# front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
# tunnel = [gamestate.places['tunnel_0_{0}'.format(i)]
#         for i in range(9)]
# tunnel[1].add_insect(back_ant)
# tunnel[7].add_insect(front_ant)
# tunnel[4].add_insect(impostor)
# impostor.action(gamestate)
# impostor.armor            # Impostors must die!

# tunnel[4].ant is None
# back_ant.damage           # Ants should not be buffed
# front_ant.damage
# tunnel[4].add_insect(queen)
# queen.action(gamestate)


# remove from case
# import ants, importlib
# importlib.reload(ants)
# beehive = ants.Hive(ants.AssaultPlan())
# dimensions = (2, 9)
# gamestate = ants.GameState(None, beehive, ants.ant_types(),
#         ants.dry_layout, dimensions)
# ants.bees_win = lambda: None
# # QueenAnt Removal
# queen = ants.QueenAnt()
# impostor = ants.QueenAnt()
# place = gamestate.places['tunnel_0_2']
# place.add_insect(impostor)
# place.remove_insect(impostor)
# place.ant is None         # Impostors can be removed
# place.add_insect(queen)
# place.remove_insect(queen)
# place.ant is queen



import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),
        ants.dry_layout, dimensions)
#
# Extensive damage doubling tests
queen_tunnel, side_tunnel = [[gamestate.places['tunnel_{0}_{1}'.format(i, j)]
        for j in range(9)] for i in range(2)]
queen = ants.QueenAnt()
queen_tunnel[7].add_insect(queen)
# Turn 0
thrower = ants.ThrowerAnt()
fire = ants.FireAnt()
side = ants.ThrowerAnt()
front = ants.ThrowerAnt()
queen_tunnel[0].add_insect(thrower)
queen_tunnel[1].add_insect(fire)
queen_tunnel[8].add_insect(front)
side_tunnel[0].add_insect(side)
# layout right now
# [thrower, fire, , , , , , queen, front]
# [side   ,     , , , , , ,      ,      ]
thrower.damage, fire.damage  = 101, 102,
front.damage, side.damage = 104, 105
queen.action(gamestate)
(thrower.damage, fire.damage)