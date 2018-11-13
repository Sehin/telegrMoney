from classes.domain.DbEntity import DbEntity


class Category(DbEntity):
    def __init__(self, id, name) -> None:
        super.__init__(id)
        self.name = name
