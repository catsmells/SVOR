class SVORAnalysis:
    def __init__(self, strengths, vulnerabilities, opportunities, risks, infrastructure, k, strategies):
        self.strengths = strengths
        self.vulnerabilities = vulnerabilities
        self.opportunities = opportunities
        self.risks = risks
        self.infrastructure = infrastructure
        self.k = k
        self.strategies = strategies

    def calculate_total_forces(self):
        total_strengths = sum(value for _, value in self.strengths)
        total_vulnerabilities = sum(value for _, value in self.vulnerabilities)
        total_opportunities = sum(value for _, value in self.opportunities)
        total_risks = sum(value for _, value in self.risks)
        total_infrastructure = sum(value for _, value in self.infrastructure)
        return total_strengths + total_vulnerabilities + total_opportunities + total_risks + total_infrastructure

    def calculate_tfgc(self):
        total_infrastructure = sum(value for _, value in self.infrastructure)
        total_opportunities = sum(value for _, value in self.opportunities)
        return total_infrastructure / total_opportunities if total_opportunities != 0 else float('inf')

    def calculate_vgc(self):
        total_forces = self.calculate_total_forces()
        return 1 / total_forces if total_forces != 0 else float('inf')

    def calculate_ogc(self):
        total_risks = sum(value for _, value in self.risks)
        return 1 / total_risks if total_risks != 0 else float('inf')

    def calculate_rgc(self):
        total_vulnerabilities = sum(value for _, value in self.vulnerabilities)
        return self.k / total_vulnerabilities if total_vulnerabilities != 0 else float('inf')

    def calculate_svor_value(self):
        tfgc = self.calculate_tfgc()
        vgc = self.calculate_vgc()
        ogc = self.calculate_ogc()
        rgc = self.calculate_rgc()
        positives = [tfgc, sum(value for _, value in self.opportunities), ogc]
        negatives = [sum(value for _, value in self.vulnerabilities), rgc, sum(value for _, value in self.risks), vgc]
        positive_sum = sum(positives)
        negative_sum = sum(negatives)
        return positive_sum / negative_sum if negative_sum != 0 else float('inf')

    def make_decision(self):
        svor_value = self.calculate_svor_value()
        if svor_value > 1:
            decision = "Consider making the decision."
        elif 0 < svor_value <= 1:
            decision = "Advisory: Reconsider the decision, but it is not outright negative."
        else:
            decision = "Reconsider the decision."
        return svor_value, decision

def input_elements(name):
    print(f"Enter the {name} elements (type 'done' when finished):")
    elements = []
    while True:
        element = input(f"- {name} element: ")
        if element.lower() == 'done':
            break
        value = float(input(f"Enter the weight for {element}: "))
        elements.append((element, value))
    return elements

def input_strategies():
    strategies = {
        "Strength-Opportunity": [],
        "Vulnerability-Opportunity": [],
        "Risk-Strength": [],
        "Risk-Vulnerability": []
    }
    for key in strategies.keys():
        print(f"Enter the strategies for {key} (type 'done' when finished):")
        while True:
            description = input(f"- {key} strategy: ")
            if description.lower() == 'done':
                break
            value = float(input(f"Enter the weight for this strategy: "))
            strategies[key].append((description, value))
    return strategies

def svor_wizard():
    decision = input("Enter the decision being analyzed: ")
    strengths = input_elements("Strengths")
    vulnerabilities = input_elements("Vulnerabilities")
    opportunities = input_elements("Opportunities")
    risks = input_elements("Risks")
    infrastructure = input_elements("Infrastructure")
    k = float(input("Enter the constant k: "))
    strategies = input_strategies()
    svor = SVORAnalysis(strengths, vulnerabilities, opportunities, risks, infrastructure, k, strategies)
    svor_value, decision_result = svor.make_decision()
    print("\nSVOR Analysis Report")
    print("====================")
    print(f"Decision: {decision}")
    print("--------------------")
    print(f"Strengths: {strengths}")
    print(f"Vulnerabilities: {vulnerabilities}")
    print(f"Opportunities: {opportunities}")
    print(f"Risks: {risks}")
    print(f"Infrastructure: {infrastructure}")
    print(f"Constant k: {k}")
    print("--------------------")
    print("Strategies:")
    for strategy, descriptions in strategies.items():
        print(f"{strategy}:")
        for description, value in descriptions:
            print(f"  - {description} (Value: {value})")
    print("--------------------")
    print(f"Calculated SVOR Value: {svor_value:.2f}")
    print(f"Decision Result: {decision_result}")
svor_wizard()
