class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Initialize our cash register
        billsOnHand = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            # Add the bill to our cash register
            billsOnHand[bill] += 1
            
            changeToReturn = bill - 5
            
            while changeToReturn > 0:
                if changeToReturn >= 10 and billsOnHand[10] > 0:
                    changeToReturn -= 10
                    billsOnHand[10] -= 1
                elif changeToReturn >= 5 and billsOnHand[5] > 0:
                    changeToReturn -= 5
                    billsOnHand[5] -= 1
                else:
                    return False

        return True
        
