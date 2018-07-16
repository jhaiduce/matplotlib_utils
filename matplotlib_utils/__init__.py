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
        if axis=='x' and (pos[0]<xmin or pos[0]>xmax) or \
           axis=='y' and (pos[1]<ymin or pos[1]>ymax):
            continue
        bbox=label.get_window_extent()
        bbox=fig.transFigure.inverted().transform(bbox)
        (x1,y1),(x2,y2)=bbox
        if axis=='y':
            if y1<ax_y1 or y2>ax_y2: label.set_visible(False)
        if axis=='x':
            if x1<ax_x1 or x2>ax_x2: label.set_visible(False)

def add_subplot_labels(ax_list,labelpos=(0.95,0.95),subplot_labels=None,**kwargs):

    if subplot_labels is None:
        from string import ascii_lowercase
        subplot_labels=[ascii_lowercase[i] for i in range(len(ax_list))]

    label_artists=[]

    # Default values
    kwargs['weight']=kwargs.get('weight','bold')
    kwargs['fontsize']=kwargs.get('fontsize',11)
    kwargs['verticalalignment']=kwargs.get('verticalalignment','top')
    kwargs['horizontalalignment']=kwargs.get('horizontalalignment','right')

    for i,ax in enumerate(ax_list):
        text=ax.text(labelpos[0],labelpos[1],subplot_labels[i],transform=ax.transAxes,**kwargs)
        label_artists.append(text)

    return label_artists
