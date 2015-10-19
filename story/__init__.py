

class Battle():
    """Classs representing a battle in the story."""

    def __init___(self,**kwargs):
        self.player = kwargs.get(player)
        self.p = self.player
        self.opponent = kwargs.get(opponent)
        self.o = self.opponent
        self.first = self.player
        self.second = self.opponent
        self.rounds = 0
        self.ended = False

    def begin(self):
        while not self.ended:
           _handle_round();

    def _decide_who_is_first():
        """Handle one round, which is one turn for each in battle."""
        p = self.player
        o = self.opponent
        n = self.rounds

        if s.rounds > 1 and s.p.speed == s.o.speed:
            s.first = s.second
            s.second = s.first
        elif s.p.speed > s.o.speed:
            s.first = s.p
            s.second = s.o
        else:
            s.second = s.player
            s.first = s.opponent
    def _handle_round(self):
        _decide_who_is_first()
