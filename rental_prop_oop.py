class Analyzing_rental_properties:
    def __init__(self, income=0, taxes=0, insurance=0, utilities=0, hoa=0, lawn_care=0, vacancy=0, repairs=0, capex=0, management=0, mortgage=0, cash_flow=0, down_payment=0, closing_costs=0, rehab=0, other=0):
        self.income = income
        self.tax = taxes 
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn_care = lawn_care
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.management = management
        self.mortgage = mortgage
        self.cash_flow = cash_flow
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab = rehab
        self.other = other 

    def rental_income(self):
        self.income = int(input('What is the projected rental income? '))

    def rental_expenses(self):
        self.taxes = int(input('How much are monthly taxes? '))
        self.insurance = int(input('How much is the monthly insurance? '))
        self.utilities = int(input('How much are the monthly utilities? '))
        self.hoa = int(input('How much is the monthly HOA? ')) 
        self.lawn_care = int(input('How much per month for lawn care? '))
        self.vacency = int(input('How much per month for vacency? (recommened 5% of projected monthly income)  '))
        self.repairs = int(input('How much monthly for projected repairs? (recommened $50-100)  '))
        self.capex = int(input('How much per month to save for the big expenses? (roof, water damage, ect... recommened $50-100)  '))
        self.management = int(input('How much to pay property manager per month? (recommened 10% of projected income)  '))
        self.mortgage = int(input("How much is your mortgage?  "))

        self.monthly_expenses = self.taxes + self.insurance + self.utilities + self.hoa + self.lawn_care + self.vacency + self.repairs + self.capex + self.management + self.mortgage

    def cf(self):
        self.cash_flow = self.income - self.monthly_expenses 
        self.annual_cash_flow = self.cash_flow * 12

    def investment(self):
        self.down_payment = int(input('How much did you put down? '))
        self.closing_costs = int(input('How much did you spend in closing costs?  '))
        self.rehab = int(input("How much did you spend to rehabilitate the house?  "))
        self.other = int(input('Any other costs associated with buying the house? '))
        
        self.total_investment = self.down_payment + self.closing_costs + self.rehab + self.other

    def return_on_investment(self):
        ROI = (self.annual_cash_flow / self.total_investment) * 100
        print('Your projected cash on cash return on investment is...', ROI)

x = Analyzing_rental_properties()
x.rental_income()
x.rental_expenses()
x.cf()
x.investment()
x.return_on_investment()