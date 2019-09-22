"""
* DEMO-4 --- Build volume meshes for the "bunny" geometry.
% Compare performance of "delaunay" + "delfront" algorithms.
*
* These examples call to JIGSAW via its cmd.-line interface.
*
* Writes "case_4x.vtk" files on output for vis. in PARAVIEW.
*
"""

from pathlib import Path
import numpy as np

import jigsawpy

def case_4_(src_path,dst_path):

    opts = jigsawpy.jigsaw_jig_t()

    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        str(Path(src_path)/"bunny.msh") # GEOM file
        
    opts.jcfg_file = \
        str(Path(dst_path)/"bunny.jig") # JCFG file
    
    opts.mesh_file = \
        str(Path(dst_path)/"bunny.msh") # MESH file
    
#------------------------------------ make mesh using JIGSAW

    opts.mesh_kern = "delaunay"         # DELAUNAY kernel
    opts.mesh_dims = +3
    
    opts.optm_iter = +0
    
    opts.hfun_hmax = 0.03
    
    jigsawpy.cmd.jigsaw(opts, mesh)

    print("Saving case_4a.vtk file.")

    jigsawpy.savevtk("case_4a.vtk",mesh)

#------------------------------------ make mesh using JIGSAW

    opts.mesh_kern = "delfront"         # DELFRONT kernel
    opts.mesh_dims = +3
    
    opts.optm_iter = +0
    
    opts.hfun_hmax = 0.03
    
    jigsawpy.cmd.jigsaw(opts, mesh)

    print("Saving case_4b.vtk file.")

    jigsawpy.savevtk("case_4b.vtk",mesh)

    return



