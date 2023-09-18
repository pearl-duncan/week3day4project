class Analyzing_rental_properties:
    def __init__(self, income):
        self.income = rental_income
        rental_income = int(input('What is the projected rental income of the property?  '))
        
    def expenses(self, tax_expenses, insurance_expenses, utilities, hoa, lawn_care, vacency, repairs, capex, management, mortgage):
        self.tax_expenses = taxes 
        taxes = int(input('How much are monthly taxes? '))
        self.insurance_expenses = insurance 
        insurance = int(input('How much is the monthly insurance? '))
        self.utilities = utilities
        utilities = int(input('How much are the monthly utilities? '))
        self.hoa = hoa
        hoa = int(input('How much is the monthly HOA? ')) 
        self.lawn_care = lawn_care
        lawn_care = int(input('How much per month for lawn care? '))
        self.vacency = vacency 
        vacency = int(input('How much per month for vacency? (recommened 5% of projected monthly income)  '))
        self.repairs = repairs
        repairs = int(input('How much monthly for projected repairs? (recommened $50-100)  '))
        self.capex = capex
        capex = int(input('How much per month to save for the big expenses? (roof, water damage, ect... recommened $50-100)  '))
        self.management = management
        management = int(input('How much to pay property manager per month? (recommened 10% of projected income)  '))
        self.mortgage = mortgage
        mortgage = int(input("How much is your mortgage?  "))

        monthly_expenses = taxes + insurance + utilities + hoa + lawn_care + vacency + repairs + capex + management + mortgage

    def cash(self, cash_flow):
        self.cash_flow = cash_flow
        cash_flow = rental_income - monthly_expenses 

    def investment(self, down_payment, closing_costs, rehab, other):
        self.down_payment = down_payment
        down_payment = int(input('How much did you put down? '))
        self.closing_costs = closing_costs
        closing_costs = int(input('How much did you spend in closing costs?  '))
        self.rehab = rehab
        rehab = int(input("How much did you spend to rehabilitate the house?  "))
        self.other = other 
        other = int(input('Any other costs associated with buying the house? '))
        
        total_investment = down_payment + closing_costs + rehab + other

        anual_cash_flow = self.cash_flow * 12

        ROI = (anual_cash_flow / total_investment) * 100
        print('Your projected cash on cash return on investment is...', ROI)