from functools import reduce


class AHash(object):

    @staticmethod
    def calculate_hash(image):
        im = image.resize((12, 8)).convert('L')
        avg = reduce(lambda x, y: x + y, im.getdata()) / 96.
        return reduce(lambda x, y_z: x | (y_z[1] << y_z[0]),
                      enumerate(
                          map(lambda i: 0 if i < avg else 1, im.getdata())),
                      0)

    @staticmethod
    def hamming_distance(h1, h2):
        h, d = 0, h1 ^ h2
        while d:
            h += 1
            d &= d - 1
        return h
