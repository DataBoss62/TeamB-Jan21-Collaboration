from budgetClasses import Budget

def test_budget():
    testBudget = Budget(100)
    assert testBudget.balance == 100
    assert testBudget == "The remaining balance of the selected budget is: £100"

def test_budget_2():  
    testBudget = Budget(200)
    testBudget.withdraw(4)
    assert testBudget.balance == 160    