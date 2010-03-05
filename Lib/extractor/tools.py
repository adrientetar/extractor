from robofab.ufoLib import fontInfoAttributesVersion2, validateFontInfoVersion2ValueForAttribute

defaultLeftKerningGroupPrefix = "@KERN_LEFT_"
defaultRightKerningGroupPrefix = "@KERN_RIGHT_"


class RelaxedInfo(object):

    """
    This object that sets only valid info values
    into the given info object.
    """

    def __init__(self, info):
        self._object = info

    def __setattr__(self, attr, value):
        if attr in fontInfoAttributesVersion2:
            if validateFontInfoVersion2ValueForAttribute(attr, value):
                setattr(self._object, attr, value)
        else:
            super(RelaxedInfo, self).__setattr__(attr, value)
