class PayoffTuple:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
    
    def __str__(self):
        return f"({self.u1}, {self.u2})"

    def __repr__(self):
        return f"({self.u1}, {self.u2})"

    def __lt__(self, other):
        # Check u1 values first
        if self.u1 < other.u1:
            if self.u2 > other.u2:
                return True
            raise ValueError(f"Items {self} and {other} are not comparable.")
        elif self.u1 > other.u1:
            if self.u2 < other.u2:
                return 
            raise ValueError(f"Items {self} and {other} are not comparable.")
        else:  # self.u1 == other.u1
            if self.u2 == other.u2:
                return False
            raise ValueError(f"Items {self} and {other} are not comparable.")
            
    def __eq__(self, other):
        return self.u1 == other.u1 and self.u2 == other.u2
