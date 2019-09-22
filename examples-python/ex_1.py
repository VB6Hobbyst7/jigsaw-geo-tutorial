
from pathlib import Path
import os
import numpy as np
from scipy import interpolate

import jigsawpy

def ex_1():

# DEMO-1: generate a uniform resolution (150KM) global grid.

    src_path = os.path.join(
        os.path.abspath(
        os.path.dirname(__file__)),"files")

    dst_path = os.path.join(
        os.path.abspath(
        os.path.dirname(__file__)),"cache")


    opts = jigsawpy.jigsaw_jig_t()

    topo = jigsawpy.jigsaw_msh_t()
    
    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()

#------------------------------------ setup files for JIGSAW

    opts.geom_file = \
        str(Path(dst_path)/"earth.msh") # GEOM file
        
    opts.jcfg_file = \
        str(Path(dst_path)/"globe.jig") # JCFG file
    
    opts.mesh_file = \
        str(Path(dst_path)/"globe.msh") # MESH file

#------------------------------------ define JIGSAW geometry

    geom.mshID = "ellipsoid-mesh"
    geom.radii = np.full(3, 6371., 
        dtype=jigsawpy.jigsaw_msh_t.REALS_t)
    
    jigsawpy.savemsh(opts.geom_file, geom)

#------------------------------------ make mesh using JIGSAW 
    
    opts.hfun_scal = "absolute"
    opts.hfun_hmax = +150.          # uniform at 150km
    
    opts.mesh_dims = +2             # 2-dim. simplexes
    
    opts.optm_qlim = +9.5E-01       # tighter opt. tol
    opts.optm_iter = +32    
    opts.optm_qtol = +1.0E-05
    
    jigsawpy.cmd.jigsaw(opts, mesh)

#------------------------------------ save mesh for Paraview

    jigsawpy.loadmsh(
        str(Path(src_path)/"topo.msh"), topo)
   
#------------------------------------ a very rough land mask

    apos = jigsawpy.R3toS2(
        geom.radii, mesh.point["coord"][:])

    apos = apos * 180./np.pi

    zfun = interpolate.RectBivariateSpline(
        topo.ygrid, topo.xgrid, topo.value)

    mesh.value = zfun(
        apos[:, 1], apos[:, 0], grid=False)

    zmsk = \
    mesh.value[mesh.tria3["index"][:,0]] + \
    mesh.value[mesh.tria3["index"][:,1]] + \
    mesh.value[mesh.tria3["index"][:,2]]
    zmsk = zmsk / +3.0

    mesh.tria3 = mesh.tria3[zmsk < +0.]

    
    print("Writing ex_a.vtk file.")

    jigsawpy.savevtk(
        str(Path(dst_path)/"ex_a.vtk"), mesh)


    return


if (__name__ == "__main__"): ex_1()



