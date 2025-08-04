# scenario.py
def generate_scenario(level):
    if level == 1:
        return "You’re at the playground and a bully has taken your ball."
    elif level == 2:
        return "Your classmate is twisting your words during a debate."
    elif level == 3:
        return "Your partner is emotionally overwhelmed during a disagreement."
    elif level == 4:
        return "You must negotiate peace with a stubborn world leader."
    return "Default conflict scenario."
