from latex2sympy2 import latex2sympy
from sympy import lambdify


class TexWithoutArgumentsError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


def latex2lambda(
    tex: str,
    variable_values={},
    args=None,
    modules=None,
    printer=None,
    use_imps=True,
    dummify=False,
):
    if args is None:
        try:
            """
            Trying to parse a function of type "f(...) = <...>" with the function itself on <...>
            """
            var_tex, tex = tex.replace(" ", "").split("=")
            args = var_tex.split("(")[1].replace(")", "").split(",")
        except Exception:
            raise TexWithoutArgumentsError(
                "No arguments provided. Either pass the arguments as list or as r'f(<args>) = <...>'."
            )

    sympy_form = latex2sympy(tex, variable_values)
    lambda_form = lambdify(
        args=args,
        expr=sympy_form,
        modules=modules,
        printer=printer,
        use_imps=use_imps,
        dummify=dummify,
    )

    return lambda_form


if __name__ == "__main__":
    test = r"f(x,a) = a*\sin(x)"
    func = latex2lambda(test)

    print(func)
