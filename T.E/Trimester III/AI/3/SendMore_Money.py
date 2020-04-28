from CSP import CSP

class SendMoreMoneyConstraint:
    def __init__(self,letters):
        self.letters = letters
    
    def satisfied(self, assignment):
        if len(set(assignment.values()))<len(assignment):
            return False
        
        if len(assignment) ==  len(self.letters):
            #Assigned values to ensure no-duplication
            s = assignment['S']
            e = assignment['E']
            n = assignment['N']
            d = assignment['D']
            m = assignment['M']
            o = assignment['O']
            r = assignment['R']
            y = assignment['Y']
            
            #Checking if condition is satisfied
            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n*100 + e * 10 + y
            
            return send + more == money
        return True

if __name__ == "__main__":
    letters = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    possible_digits = { }

    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_digits["M"] = [1]  # so we don't get answers starting with a 0

    csp = CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))

    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for key, val in solution.items():
            print(str(key).ljust(10), str(val).ljust(30))