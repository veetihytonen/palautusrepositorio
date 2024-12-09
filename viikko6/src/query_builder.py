from matchers import And, Or, Not, All, PlaysIn, HasAtLeast, HasFewerThan 

class QueryBuilder():
    def __init__(self, queries: None | list = None):
        if not queries:
            self.queries = []
        else:
            self.queries = queries

    def plays_in(self, team: str):
        return QueryBuilder([q for q in self.queries].append(PlaysIn(team)))

    def has_at_least(self, value, atrr):
        return QueryBuilder([q for q in self.queries].append(HasAtLeast(value=value, attr=atrr)))
    
    def has_fewer_than(self, value, atrr):
        return QueryBuilder([q for q in self.queries].append(HasFewerThan(value=value, attr=atrr)))

    def one_of(q1, q2):
        return QueryBuilder([Or(q1, q2)])

    def build(self):
        if not self.queries:
            return All()

        if len(self.queries) == 1:
            return self.queries[0]
        
        return And(self.queries)
    
