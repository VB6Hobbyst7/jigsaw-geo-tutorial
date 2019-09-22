function plotplanar(geom,mesh,hfun)
%PLOT-PLANAR draw JIGSAW output for meshes on planes.
  
    if (~isempty(geom))
%------------------------------------ draw domain boundaries
        figure('color','w');
        patch ('faces',geom.edge2.index(:,1:2), ...
            'vertices',geom.point.coord(:,1:2), ...
            'facecolor','w', ...
            'edgecolor',[.1,.1,.1], ...
            'linewidth',1.5) ;
        hold on; axis image;
        title('JIGSAW GEOM data') ;
    end

    if (~isempty(hfun))
    switch (upper(hfun.mshID))
        case{'EUCLIDEAN-GRID', ...
             'ELLIPSOID-GRID'}
%------------------------------------ disp. 'grid' functions
        hfun.value = reshape(hfun.value, ...
            length(hfun.point.coord{2}), ...
            length(hfun.point.coord{1})  ...
            ) ;
        figure('color','w') ;
        surf(hfun.point.coord{1}, ...
             hfun.point.coord{2}, ...
             hfun.value) ;
        view(2); axis image; hold on ;
        shading interp;
        title('JIGSAW HFUN data') ;
        
        case{'EUCLIDEAN-MESH', ...
             'ELLIPSOID-MESH'}
%------------------------------------ disp. 'mesh' functions
        figure('color','w') ;
        patch ('faces',hfun.tria3.index(:,1:3), ...
            'vertices',hfun.point.coord(:,1:2), ...
            'facevertexcdata',hfun.value, ...
            'facecolor','flat', ...
            'edgecolor','none') ;
        view(2); axis image; hold on ;
        title('JIGSAW HFUN data') ;      
    end 
    end

    if (~isempty(mesh))
%------------------------------------ draw unstructured mesh
        figure('color','w');
        P = mesh.tria3.index (:,4);
        if ( all (P == +0))
        patch ('faces',mesh.tria3.index(:,1:3), ...
            'vertices',mesh.point.coord(:,1:2), ...
            'facecolor','w', ...
            'edgecolor',[.2,.2,.2]) ;
        hold on; axis image;    
        else
        for ip = 1 : max(P)
        I = P == ip;
        patch ('faces',mesh.tria3.index(I,1:3), ...
            'vertices',mesh.point.coord(:,1:2), ...
            'facecolor', rand(1,3), ...
            'edgecolor',[.2,.2,.2]) ;
        hold on; axis image;
        end
        end
        patch ('faces',mesh.edge2.index(:,1:2), ...
            'vertices',mesh.point.coord(:,1:2), ...
            'facecolor','w', ...
            'edgecolor',[.1,.1,.1], ...
            'linewidth',1.5) ;
        if (~isempty(geom))
        patch ('faces',geom.edge2.index(:,1:2), ...
            'vertices',geom.point.coord(:,1:2), ...
            'facecolor','w', ...
            'edgecolor',[.1,.1,.8], ...
            'linewidth',1.5) ;
        end
        title('JIGSAW TRIA mesh') ;

        drawcost (mesh,hfun) ;
    end
    
end



