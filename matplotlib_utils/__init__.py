def remove_overhanging_labels(ax,fig,axis='y'):
    """
    Removes any tick labels that overhang the end of the axis. This is useful when subplots have been arranged very tightly, in which case overhanging tick labels may conflict with adjacent subplots.

    Note: draw() must be called on the matplotlib canvas object before calling this function, so that the tick labels exist and have bounding boxes in order to check whether they overhaing the axis.

    ax: Axes object to operate on
    fig: Figure that ax resides in
    axis: Which axis to operate on ('x' or 'y')
    """

    # Get the tick labels
    if axis=='x':
        labels=ax.xaxis.get_ticklabels()
    elif axis=='y':
        labels=ax.yaxis.get_ticklabels()
    else:
        raise ValueError('axis argument must be ''x'' or ''y''.')

    # Get axis bounding box
    ax_bbox=ax.get_position()
    ax_x1,ax_y1,ax_x2,ax_y2=ax_bbox.extents

    for label in labels:

        # Get label position
        pos=label.get_position()

        # Check that tick is within the axis limits
        # (if it isn't, it won't be drawn anyway and there is nothing to do)
        xmin,xmax=ax.get_xlim()
        ymin,ymax=ax.get_ylim()
        if axis=='x' and (pos[0]<xmin or pos[0]>xmax) or \
           axis=='y' and (pos[1]<ymin or pos[1]>ymax):
            continue

        # Get label bounding box
        bbox=label.get_window_extent()
        bbox=fig.transFigure.inverted().transform(bbox)
        (x1,y1),(x2,y2)=bbox

        # Check label bounds against axes bounds, hide label if needed
        if axis=='y':
            if y1<ax_y1 or y2>ax_y2: label.set_visible(False)
        if axis=='x':
            if x1<ax_x1 or x2>ax_x2: label.set_visible(False)

def add_subplot_labels(ax_list,labelpos=(0.95,0.95),subplot_labels=None,**kwargs):
    """
    Add alphanumeric (or custom) labels to a set of Axes objects. For an array of Axes objects, label each 'a', 'b', 'c', etc. (or a specified sequence of strings).

    ax_list: List of Axes objects
    labelpos: Label position, in Axes coordinates
    subplot_labels: Sequence of strings or None. Default is None, which results in alphanumeric labels ('a', 'b', 'c', etc.)
    
    Any remaining arguments are passed on to matplotlib.axes.Axes.text() to format the labels.

    Returns: Sequence of Artist objects created for the labels
    """
    
    If subplot_labels is None:

        # Generate a sequence of alphanumeric labels
        from string import ascii_lowercase
        subplot_labels=[ascii_lowercase[i] for i in range(len(ax_list))]

    label_artists=[]

    # Default values for text kwargs
    kwargs['weight']=kwargs.get('weight','bold')
    kwargs['fontsize']=kwargs.get('fontsize',11)
    kwargs['verticalalignment']=kwargs.get('verticalalignment','top')
    kwargs['horizontalalignment']=kwargs.get('horizontalalignment','right')

    for i,ax in enumerate(ax_list):

        # Place the label
        text=ax.text(labelpos[0],labelpos[1],subplot_labels[i],transform=ax.transAxes,**kwargs)
        
        label_artists.append(text)

        # Invisible point to prevent legend being drawn on top of label when using loc='best'
        ax.plot(labelpos[0],labelpos[1],linestyle='',transform=ax.transAxes)

    return label_artists
