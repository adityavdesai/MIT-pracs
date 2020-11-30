class CSP:
    def __init__(self,variables,domain):
        self.variables = variables     # variables to be constrained
        self.domain = domain           # Domain of each variable
        self.constraints ={}
        
        for var in self.variables:
            self.constraints[var] = []
            if var not in self.domain:
                raise LookupError("Domain Assignment Error")
                
    def add_constraint(self,constraint):
        for v in constraint.letters:
            if v not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[v].append(constraint)
                
    def consistent(self,variable,assignment):
        #Checking all the constraints
        for cons in self.constraints[variable]:
            if not cons.satisfied(assignment):
                return False
        return True

    def backtracking_search(self,assignment={}):
        '''To run a backtracking algorithm with constraints'''
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        
        for value in self.domain[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first,local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None
