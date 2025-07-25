def generate_tip(goals, dangerous_attacks, shots_on_target):
    """
    Egyszerű predikciós algoritmus,
    amely visszaadja, hogy Over vagy Under 2.5 gól a tipp.
    """
    score = goals + 0.1 * dangerous_attacks + 0.3 * shots_on_target
    if score > 3.5:
        return "Over 2.5"
    else:
        return "Under 2.5"
Add predictor module with generate_tip function
