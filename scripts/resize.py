import numpy as np
from scipy import misc, ndimage
import os
from multiprocessing.dummy import Pool as ThreadPool

resized_image_dir="tf_files/star_wars/yoda2"

if not os.path.exists(resized_image_dir):
    os.mkdir(resized_image_dir)

def resize(image_file):
    ''' Assuming input from /train to /train_resized'''
    pic = misc.imread(os.path.join("tf_files/star_wars/yoda",image_file))

    #New dimensions
    n_dim1=299
    n_dim2=299

    picResized = misc.imresize(pic, (n_dim1, n_dim2))
    misc.imsave(os.path.join(resized_image_dir, image_file+".jpg"), picResized)
    print("Resized",image_file)

pool = ThreadPool(100)
results = pool.starmap(resize, zip(os.listdir("tf_files/star_wars/yoda")))
