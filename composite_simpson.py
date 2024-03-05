import sympy as sp




def integrate_simpson(a, b, equation, n_values):
    x = sp.Symbol('x')
    parsed_eq = sp.sympify(equation)

    def divide_interval(a, b, n_values):
        points = []
        for n in n_values:
            h = (b - a) / (2*n)
            interval_points = [a + i * h for i in range(2*n)]
            interval_points.append(b)  # Include b in the interval points
            points.append(interval_points)
        return points

    def calculate(points, parsed_eq):
        h = points[1] - points[0]
        first_point, *middle_points, last_point = points
        middle_points_even = middle_points[1::2]
        middle_points_odd = middle_points[::2]
        first_result = parsed_eq.subs(x, first_point).evalf()
        last_result = parsed_eq.subs(x, last_point).evalf()
        middle_odd_results = [parsed_eq.subs(x,point).evalf() for point in middle_points_odd]
        middle_even_results = [parsed_eq.subs(x,point).evalf() for point in middle_points_even]
        total_sum = first_result + 4*(sum(middle_odd_results)) + 2*(sum(middle_even_results)) + last_result
        return total_sum*(h/3)

    def print_calculate(a, b, n_values, parsed_eq):
        points = divide_interval(a, b, n_values)
        for idx, interval_points in enumerate(points, start=1):
            result = calculate(interval_points, parsed_eq)
            print(f"For n = {n_values[idx - 1]}, result = {result}")

    print_calculate(a, b, n_values, parsed_eq)

