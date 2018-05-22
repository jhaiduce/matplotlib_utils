def remove_overhanging_labels(ax,fig,axis='y'):
    if axis=='x':
        labels=ax.xaxis.get_ticklabels()
    elif axis=='y':
        labels=ax.yaxis.get_ticklabels()
    else:
        raise ValueError('axis argument must be ''x'' or ''y''.')
    ax_bbox=ax.get_position()
    ax_x1,ax_y1,ax_x2,ax_y2=ax_bbox.extents
    for label in labels:
        pos=label.get_position()
        xmin,xmax=ax.get_xlim()
        ymin,ymax=ax.get_ylim()
        if pos[0]<xmin or pos[0]>xmax or pos[1]<ymin or pos[1]>ymax:
            continue
        bbox=label.get_window_extent()
        bbox=fig.transFigure.inverted().transform(bbox)
        (x1,y1),(x2,y2)=bbox
        if axis=='y':
            if y1<ax_y1 or y2>ax_y2: label.set_visible(False)
        if axis=='x':
            if x1<ax_x1 or x2>ax_x2: label.set_visible(False)

