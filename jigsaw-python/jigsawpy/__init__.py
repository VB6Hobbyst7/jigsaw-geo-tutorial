r"""
------------------------------------------------------------
 *
 *   ,o, ,o,       /                                
 *    `   `  e88~88e  d88~\   /~~~8e Y88b    e    /
 *   888 888 88   88 C888         88b Y88b  d8b  / 
 *   888 888 "8b_d8"  Y88b   e88~-888  Y888/Y88b/  
 *   888 888  /        888D C88   888   Y8/  Y8/   
 *   88P 888 Cb      \_88P   "8b_-888    Y    Y     
 * \_8"       Y8""8D                                
 *
------------------------------------------------------------
 * JIGSAW: Interface to the JIGSAW meshing library.
------------------------------------------------------------
 *
 * Last updated: 05 September, 2019
 *
 * Copyright 2019 --
 * Darren Engwirda
 * darren.engwirda@columbia.edu
 * https://github.com/dengwirda
 *
------------------------------------------------------------
 *
 * This program may be freely redistributed under the 
 * condition that the copyright notices (including this 
 * entire header) are not removed, and no compensation 
 * is received through use of the software.  Private, 
 * research, and institutional use is free.  You may 
 * distribute modified versions of this code UNDER THE 
 * CONDITION THAT THIS CODE AND ANY MODIFICATIONS MADE 
 * TO IT IN THE SAME FILE REMAIN UNDER COPYRIGHT OF THE 
 * ORIGINAL AUTHOR, BOTH SOURCE AND OBJECT CODE ARE 
 * MADE FREELY AVAILABLE WITHOUT CHARGE, AND CLEAR 
 * NOTICE IS GIVEN OF THE MODIFICATIONS.  Distribution 
 * of this code as part of a commercial system is 
 * permissible ONLY BY DIRECT ARRANGEMENT WITH THE 
 * AUTHOR.  (If you are not directly supplying this 
 * code to a customer, and you are instead telling them 
 * how they can obtain it for free, then you are not 
 * required to make any arrangement with me.) 
 *
 * Disclaimer:  Neither I nor: Columbia University, The
 * Massachusetts Institute of Technology, The 
 * University of Sydney, nor The National Aeronautics
 * and Space Administration warrant this code in any 
 * way whatsoever.  This code is provided "as-is" to be 
 * used at your own risk.
 *
------------------------------------------------------------
 """

from jigsawpy.msh_t import jigsaw_msh_t
from jigsawpy.jig_t import jigsaw_jig_t
from jigsawpy.def_t import jigsaw_def_t
from jigsawpy.prj_t import jigsaw_prj_t

from jigsawpy.loadmsh import loadmsh
from jigsawpy.savemsh import savemsh
from jigsawpy.loadjig import loadjig
from jigsawpy.savejig import savejig

from jigsawpy.certify import certify

from jigsawpy.project import project
from jigsawpy.bisect  import bisect
from jigsawpy.extrude import extrude

from jigsawpy import jigsaw, libsaw

from jigsawpy.tools.predicate import trivol2, trivol3, \
    normal1, normal2, orient1, orient2

from jigsawpy.tools.scorecard import triscr2, triscr3, \
    trideg2, trideg3, triang2, triang3

from jigsawpy.tools.projector import stereo3

from jigsawpy.tools.mathutils import R3toS2, S2toR3

from jigsawpy.parse.saveoff import saveoff
from jigsawpy.parse.savewav import savewav
from jigsawpy.parse.savevtk import savevtk

class cmd:
#--------------------------------- expose cmd-line interface
    @staticmethod    
    def jigsaw(opts,mesh=None):
        
        return jigsaw.jigsaw(opts,mesh)

    @staticmethod
    def tripod(opts,tria=None):
        
        return jigsaw.tripod(opts,tria)

    @staticmethod
    def marche(opts,ffun=None):
        
        return jigsaw.marche(opts,ffun)

    @staticmethod
    def jitter(opts,imax,ibad=1,
               mesh=None):

        return jigsaw.jitter(opts,imax,
                             ibad,mesh)

    @staticmethod
    def tetris(opts,nlev,mesh=None):

        return jigsaw.tetris(opts,nlev,
                             mesh)

class lib:
#--------------------------------- expose api-lib. interface
    @staticmethod    
    def jigsaw(opts,geom,mesh,
               init=None,
               hfun=None):
        
        return libsaw.jigsaw(opts,geom,
                             mesh,init,
                             hfun)

    @staticmethod
    def tripod(opts,init,tria,
               geom=None):
        
        return libsaw.tripod(opts,init,
                             tria,geom)

    @staticmethod
    def marche(opts,ffun):
        
        return libsaw.marche(opts,ffun)



