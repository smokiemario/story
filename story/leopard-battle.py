"""Leopard battle

Blah
"""

class Leopard():
    attack = 70
    hp = 88
    spatk = 65
    spdef = 57
    defence = 53
    speed = 98
    xp = 10



def parse(s):
    action = s.action_line

    if not s.battle:
        s.battle = Battle(Leopard())

    action = s.action_line
    ended = s.battle.ended
    if ended == 'won':
        s.say("You are victorious!")
        s.player.xp += s.battle.leopard.xp
        s.action = "battlewon"
    if ended:
        s.say("The battle ended.")
        s.part = "battle-lost"
        if not s.battle:
        s.battle = Battle(Leopard())
