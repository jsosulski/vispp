from matplotlib.backends.backend_pdf import PdfPages


def better_savefig(fig, figfile, format="pdf", **kwargs):
    """To be used instead of .savefig

    This function saves pdfs without creation date. So subsequent
    overwrites of pdf files does not cause e.g. git modified.
    """
    if format == "pdf":
        with PdfPages(figfile, metadata={"CreationDate": None}) as pdf:
            pdf.savefig(fig, **kwargs)
    else:
        fig.savefig(figfile, **kwargs)
