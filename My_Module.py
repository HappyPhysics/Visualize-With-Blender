# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:29:26 2017

@author: Salem

sys.path.append("E:\Anaconda\envs\conda-python-blender\Lib\site-packages")

import os, sys; sys.path.append(os.path.dirname(bpy.data.filepath)); sys.path.append("E:\Anaconda\Lib\site-packages");import My_Module
import importlib; importlib.reload(My_Module); My_Module.go()

"""
import sys
sys.path.append("C:\Program Files\Blender Foundation\Blender\2.79\scripts")
import bpy

position_array = [(i,j,k) for i in range(5) for j in range(3) for k in range(4)]

def go():
    for pos in position_array:
        bpy.ops.mesh.primitive_uv_sphere_add(location=pos)
        bpy.ops.transform.resize(value=(0.2,0.2,0.2))