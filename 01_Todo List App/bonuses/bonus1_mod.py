def get_state_water(temp):

    LIQUID_TEMP = 0
    GAS_TEMP = 100

    if temp < LIQUID_TEMP:
        state = 'Solid'
    elif temp > GAS_TEMP:
        state = 'Gas'
    else:
        state = 'Liquid'
    return state
