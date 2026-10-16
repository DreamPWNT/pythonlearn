def outer_function():
    outer_var = "outer"

    def middle_function():
        middle_var = "middle"

        def inner_function():
            nonlocal outer_var, middle_var
            outer_var = "modified outer"
            middle_var = "modified middle"

        inner_function()
        print(middle_var)
        print(outer_var)

    middle_function()

    print(outer_var)


outer_function()
outer_function()
outer_function()
