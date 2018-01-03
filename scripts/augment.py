'''
Augmentor
'''

import Augmentor
from multiprocessing.dummy import Pool
import os
import shutil

pool = Pool(8)

paths=["./tf_files/star_wars/yoda","./tf_files/star_wars/darth_vader"] #,"./Database/Flickr_Material/glass"\
#,"./Database/Flickr_Material/plastic","./Database/Flickr_Material/organic"]

if not os.path.exists(os.path.join(paths[0],"output")):
    for path in paths:

        p = Augmentor.Pipeline(path)
        p.rotate90(probability=0.5)
        p.rotate270(probability=0.5)
        p.flip_left_right(probability=0.8)
        p.flip_top_bottom(probability=0.3)
        #p.crop_random(probability=1, percentage_area=0.5)
        p.resize(probability=1.0, width=120, height=120)
        p.shear(probability=0.4,max_shear_left=10,max_shear_right=10)
        p.skew(0.4,0.3)
        p.skew_corner(0.4,0.3)
        p.skew_tilt(0.4,0.3)
        p.histogram_equalisation(probability=0.3)
        p.random_distortion(probability=0.3, grid_width=4, grid_height=4, magnitude=5)
        p.random_erasing(probability=0.05, rectangle_area=0.12)
        p.sample(10000)

paths_output=["./tf_files/star_wars/yoda/output","./tf_files/star_wars/darth_vader/output"]
paths_output_moved=["./tf_files/star_wars_2/yoda","./tf_files/star_wars_2/darth_vader"]

def mover(file_name,paths_output,paths_output_moved):
    shutil.move(os.path.join(paths_output,file_name),os.path.join(paths_output_moved,file_name))

for j in range(2):
    List=os.listdir(paths_output[j])
    List1=[paths_output[j] for i in range(len(List))]
    List2=[paths_output_moved[j] for i in range(len(List))]
    pool.starmap(mover,zip(List,List1,List2))

for path in paths_output:
    shutil.rmtree(path)

for path in paths_output_moved:
    shutil.rmtree(os.path.join(path,"0"))
