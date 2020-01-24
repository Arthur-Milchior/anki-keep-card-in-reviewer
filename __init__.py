from aqt.main import AnkiQt

oldRequireReset = AnkiQt.requireReset
def requireReset(self: AnkiQt, modal: bool =False):
    "Signal queue needs to be rebuilt when edits are finished or by user."
    if self.state == "review":
        assert(self.reviewer.card)
        mod = self.col.db.scalar("select mod from notes where id = ?", self.reviewer.card.nid)
        if mod == self.reviewer.card.note().mod:
            # If the card still exists and did not change, stay in reviwer
            return
    oldRequireReset(self, modal)
AnkiQt.requireReset = requireReset
