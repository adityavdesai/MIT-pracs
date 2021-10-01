class Variable:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Constant:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Rel:
    """
    type(name) = list
    """

    def __init__(self, name, args):
        self.name = name
        self.value = str(self.name) + str([i.value for i in args])
        self.args = args


def unify_algo(L1, L2, testset):
    """
    L1 and L2 can be Rel, Variable or Constant types
    """
    # If both are variable or constants
    if isinstance(L1, Variable) or isinstance(L2, Variable) or isinstance(L1, Constant) or isinstance(L2, Constant):
        if L1 == L2:
            return None
        elif isinstance(L1, Variable):
            if isinstance(L2, Variable):
                print("Mismatching variables L1 and L2")
                return False
            else:
                if L1.value not in testset.values():
                    return [L2, L1]
                else:
                    print("Ambiguous")
                    return False
        elif isinstance(L2, Variable):
            if isinstance(L1, Variable):
                print("Mismatching variables L1 and L2")
                return False
            else:
                if L2.value not in testset.values():
                    return [L1, L2]
                else:
                    print("Ambiguous")
                    return False
        else:
            print("Mismatch")
            return False
    # Ensuring the functions are the same
    elif L1.name != L2.name:
        print("Relation Mismatch")
        return False
    # Ensuring the functions have the same number of arguments
    elif len(L1.args) != len(L2.args):
        print("Arguements length missmatch")
        return False
    subset = {}
    for i in range(len(L1.args)):
        S = unify_algo(L1.args[i], L2.args[i], subset)
        if not S:
            return False
        if S is not None:
            subset[S[0].value] = S[1].value
    return subset


if __name__ == "__main__":
    print(
        unify_algo(
            Rel("Knows", [Constant("Alok"), Variable("X")]),
            Rel("Knows", [Variable("Y"), Rel("Mother", [Variable("Y")])]),
            {},
        )
    )
    print()
    print(
        unify_algo(
            Rel("Knows", [Constant("Alok"), Variable("X")]), Rel("Knows", [Variable("Y"), Constant("Suzie")]), {}
        )
    )
    print()
    print(
        unify_algo(
            Rel("Knows", [Constant("Alok"), Variable("X")]), Rel("Knows", [Variable("X"), Constant("Suzie")]), {}
        )
    )
