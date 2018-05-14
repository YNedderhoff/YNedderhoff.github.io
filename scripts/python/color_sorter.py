### https://stackoverflow.com/questions/8915113/sort-hex-colors-to-match-rainbow

import colorsys

def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")   # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in xrange(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)

color_list = ["#8BC35A", "#00ACEE", "#000000", "#0077b5", "#FD6F31", "#FC561F", "#23364B", "#DBD2BF", "#FC4820", "#0077b5", "#F27F33", "#D7D0BF"]
color_list.sort(key=get_hsv)
print color_list