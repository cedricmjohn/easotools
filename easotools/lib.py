import easotools.plots as ep

def try_me():
    fig, axes=plt.subplots(1,2, figsize=(11,5))
    clean_data['grouping']=['Bd-2 and H4','CF samples','CF samples','Bd-2 and H4']
    symbols=['*','s']
    colors=['red','blue']
    ep.plot_bulk(clean_data,use_CI=False, axis=axes[0],groups='grouping',markers=symbols,marker_size=5)
    ep.plot_bulk(clean_data,use_CI=True,axis=axes[1],groups='grouping',markers=symbols,marker_size=5)
    plt.savefig("bulk_isotopes.png")
    plt.show()