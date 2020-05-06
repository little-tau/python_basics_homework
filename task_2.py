def get_user_info(f_name, l_name, birth, l_city, email, phone):
    """ Returns the user info as a single string. """
    return " ".join([f_name, l_name, birth, l_city, email, phone])


def get_user_info_kw(pars, **kwargs):
    """
    Returns the user info as a single string.
    Arguments:
        kwargs - user input
        pars - the list of parameters to output (e.g. "f_name", "l_name", "birth")
    """
    result = [kwargs[x] for x in pars]
    return " ".join(result)


# Input user data
ui_dict = {"firstname": None, "lastname": None, "birth date": None, "city": None, "email": None, "phone": None}
ui_params = ["f_name", "l_name", "birth", "l_city", "email", "phone"]
for i in ui_dict.keys():
    ui_dict[i] = input(f"Input {i}: ")

# Function call using explicit arguments
ui = get_user_info(f_name=ui_dict.get('firstname'),
                   l_name=ui_dict.get('lastname'),
                   birth=ui_dict.get('birth date'),
                   l_city=ui_dict.get('city'),
                   email=ui_dict.get('city'),
                   phone=ui_dict.get('phone'))
print(f"The user info is (explicit): {ui}")

# Function call using **kwargs
ui_kw = get_user_info_kw(pars=ui_params,
                         f_name=ui_dict.get('firstname'),
                         birth=ui_dict.get('birth date'),
                         l_name=ui_dict.get('lastname'),
                         l_city=ui_dict.get('city'),
                         email=ui_dict.get('city'),
                         phone=ui_dict.get('phone'),
                         s_else='something else')
print(f"The user info is (kwargs): {ui_kw}")
