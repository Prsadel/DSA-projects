class NoBinFoundException(Exception):
    def __init__(self):
        # print("ntplo")
        super().__init__("No Bin found to store the given object")