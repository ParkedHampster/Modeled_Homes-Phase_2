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