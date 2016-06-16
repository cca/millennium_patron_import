# See Millennium Circulation > Admin > Parameters > Circulation > Patron Type
# 3-digit, 000 to 255
ptype = {
    'UG': '001',
    'GR': '002'
}

# See Millennium Circulation > Admin > Parameters > Circulation > Pcode 3
# 3-digit, 000 to 255
pcode3 = {
    'ANIMA.BFA': '001',
    'ARCHT.BARC': '002',
    # Civic Innovation MBA, introduced Fall 2015
    # combine with Design MBA which iniated the program
    'CIMBA.MBA': '020',
    'CERAM.BFA': '003',
    'COMIC.MFA': '023',
    'COMAR.BFA': '004',
    'CURPR.MA': '017',
    # combo Design MFA + Design Strategy MBA dual degree, we put with Design
    'DD2ST': '024',
    'DESGN.MFA': '024',
    'DESST.MBA': '020',
    # these DVC** "programs" are for dual-degree grad students
    # we arbitrarily choose to capture the non-VCS side of the degree for now
    'DVCCP': '017',  # Dual Degree Vis. Crit/Curatorial Practice
    'DVCFA': '026',  # Dual Degree Vis. Crit/Fine Arts
    'DVCWR': '027',  # Dual Degree Vis. Crit/Writing
    #'EXTED': '   ',  # extended, leave null
    'FASHN.BFA': '005',
    'FCERM.MFA': '026',  # a few Fine Art MFAs share codes with their BFAs
    'FDRPT.MFA': '026',  # Drawing / Painting
    'FGLAS.MFA': '026',
    'FILMG.MFA': '025',
    'FILMS.BFA': '006',
    'FINAR.MFA': '026',
    'FLVID.BFA': '006',  # Film/Video BFA, classify with Film BFA, why does this exist?
    'FMEDA.MFA': '026',
    'FPHOT.MFA': '026',
    'FPRNT.MFA': '026',
    'FRNTR.BFA': '007',
    'FSCUL.MFA': '026',
    'FSOCP.MFA': '026',  # social practice, lump into MFA Fine Arts
    'FTEXT.MFA': '026',
    'GLASS.BFA': '008',
    'GRAPH.BFA': '009',  # if a few places we have BFA & MFA programs
    'GRAPH.MFA': '009',  # under the same PCODE number
    'ILLUS.BFA': '010',
    'INACT.MFA': '024',  # plain ol' Design MFA, not Interaction Design
    'INDIV.BFA': '011',
    'INDUS.BFA': '012',
    'INDUS.MFA': '012',
    'INTER.BFA': '014',
    # Master's of Design in Interaction Design, new 2015
    # classify with Interaction Design BFA
    'IXDGR.MDES': '013',
    'IXDSN.BFA': '013',
    'MAAD1.MAAD': '019',
    'MAAD2.MAAD': '019',
    'MAAD3.MAAD': '019',
    'MARC2.MARC': '016',
    'MARC3.MARC': '016',
    'METAL.BFA': '015',
    #'NODEG.UG': '   ',  # no degree, leave null
    'PHOTO.BFA': '029',
    'PNTDR.BFA': '028',
    'PPMBA.MBA': '021',  # Public Policy MBA
    #'PRECO': '   ',  # leave null, pre-college
    'PRINT.BFA': '030',
    'SCULP.BFA': '031',
    'SFMBA.MBA': '022',  # Strategic Foresight MBA
    'SOCPR.MA': '036',  # Social Practice MA, new Fall 2016
    'TEXTL.BFA': '032',
    'UNDEC.BFA': '033',
    'VISCR.MA': '018',
    'VISST.BA': '034',
    'WRITE.MFA': '027',
    'WRLIT.BA': '035'
}
