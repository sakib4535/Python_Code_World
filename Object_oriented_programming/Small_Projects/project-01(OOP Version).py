class Polynomial:

    def __init__(self, poly):
        self.poly = poly

    def differentiate(self):
        terms = self.poly.split('+')
        derivative_terms = []

        for term in terms:
            if 'x' in term:
                coefficient, power = term.split('x')
                if coefficient == '':
                    coefficient = '1'
                if power == '':
                    power = 1
                else:
                    power = power[1:]
                power = int(power)
                derivative_coefficient = int(coefficient) * power
                derivative_power = power - 1
                if derivative_power == 0:
                    derivative_term = str(derivative_coefficient)
                elif derivative_power == 1:
                    derivative_term = f"{derivative_coefficient}x"
                else:
                    derivative_term = f"{derivative_coefficient}x^{derivative_power}"
            else:
                derivative_term = '0'

            derivative_terms.append(derivative_term)
        derivative = '+'.join(derivative_terms)
        return derivative

poly = Polynomial('3x^4+2x^3+5x^2+7x+9')
derivative = poly.differentiate()
print(derivative)



