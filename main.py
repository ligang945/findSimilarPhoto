#!/usr/bin/python

import os
import sys

from PIL import Image

from src.dHash import DHash

EXTS = '.jpg', '.jpeg', '.gif', '.png'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s [dir]" % sys.argv[0])
        exit(1)

    wd = sys.argv[1]

    images = []
    for root, dirs, fs in os.walk(wd):
        for f in fs:
            if os.path.splitext(f)[1] in EXTS:
                images.append(os.path.join(root, f))

    print("calculating hash...")
    hashPath = {}
    for image in images:
        h = DHash.calculate_hash(Image.open(image))
        # h = AHash.calculate_hash(Image.open(image))

        if h in hashPath:
            print("same photo: %s ---- %s" % (image, hashPath[h]))
        else:
            hashPath.setdefault(h, image)

    print("calculating hamming distance...")
    keys = list(hashPath.keys())
    for i in range(0, len(keys)):
        for j in range(i + 1, len(keys)):
            dis = DHash.hamming_distance(keys[i], keys[j])  # choose dHash
            # dis = AHash.hamming_distance(keys[i], keys[j])  # choose aHash
            if dis < 5:
                print("similar photo: %s ---- %s" %
                      (hashPath[keys[i]], hashPath[keys[j]]))
