import os
import sys
import argparse
import tensorflow as tf
from PIL import Image

def convert_images(path_images):
    for root, dirs, files in os.walk(path_images):
        for filename_src in files:
            stem, extension = os.path.splitext(filename_src)
            if extension.lower() != '.jpg':
                continue

            pathname_jpg = os.path.join(root, filename_src)
            with tf.io.gfile.GFile(pathname_jpg, 'rb') as fid:
                encoded_jpg = fid.read(4)

            # png
            if encoded_jpg[:4] == b'\x89PNG':
                print('png:{}'.format(filename_src))
                pathname_png = os.path.join(root, '{}.png'.format(stem))
                tf.io.gfile.copy(pathname_jpg, pathname_png, True)
                Image.open(pathname_png).convert('RGB').save(pathname_jpg, 'jpeg')

            # gif
            elif encoded_jpg[:3] == b'GIF':
                print('gif:{}'.format(filename_src))
                pathname_gif = os.path.join(root, '{}.gif'.format(stem))
                tf.io.gfile.copy(pathname_jpg, pathname_gif, True)
                Image.open(pathname_gif).convert('RGB').save(pathname_jpg, 'jpeg')

            elif not (encoded_jpg[:2] == b'\xff\xd8' and encoded_jpg[2:4] == b'\xff'):
                print('not jpg:{}'.format(filename_src))

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('path_images', type=str, help='Path to the images directory')
    args = parser.parse_args(argv[1:])
    
    convert_images(args.path_images)

if __name__ == "__main__":
    sys.exit(int(main(sys.argv) or 0))


# credit to: https://github.com/tensorflow/models/issues/2194#issuecomment-401979962
