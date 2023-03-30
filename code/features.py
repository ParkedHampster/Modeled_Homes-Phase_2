def has_feature(feature):
    """
    For parsing an array of square footages as floats,
    returns 1 if the number is greater than 0 and
    returns 0 if the value is 0 or less


    Args:
        feature (float): number indicating square footage of a given feature

    Returns:
        int: 1 or 0 indicating the existence of a feature
    """

    # the +0 at the end of this line coerces the boolean
    # value from True or False to 1 or 0 respectively
    return (feature>0)+0

def ytick_convert(count,by):
    tickrange = range(by,count*by+1,by)
    tick_vals = [value for value in tickrange]
    converted_ticks = [f'${value/1000000:.1f}M' for value in tick_vals]
    return (
        tick_vals, converted_ticks
    )