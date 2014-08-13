# See Millennium Circulation > Admin > Parameters > Circulation > Patron Type
# 3-digit, 000 to 255
ptype = {'UG': '001', 'GR': '002'}

# See Millennium Circulation > Admin > Parameters > Circulation > Pcode 3
# 3-digit, 000 to 255
# ?s = VCS, MFA Comics, MAAD2&3
pcode3 = {
    'ANIMA.BFA': '001',
    'ARCHT.BARC': '002',
    'CERAM.BFA': '003',
    'COMAR.BFA': '004',
    'CURPR.MA': '017',
    'DD2ST': '024',  # single oddity which we classify into Design MFA
    'DESGN.MFA': '024',
    'DESST.MBA': '020',
    'DVCFA': '   ',  # @todo what's this program?
    'EXTED': '   ',  # extended, leave null
    'FASHN.BFA': '005',
    'FCERM.MFA': '026',  # several Fine Art MFAs share codes with their BFAs
    'FDRPT.MFA': '026',  # Drawing / Painting
    'FGLAS.MFA': '026',
    'FILMG.MFA': '025',
    'FILMS.BFA': '006',
    'FINAR.MFA': '026',
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
    'INACT.MFA': '013',  # Interaction Design MFA
    'INDIV.BFA': '011',
    'INDUS.BFA': '012',
    'INDUS.MFA': '012',
    'INTER.BFA': '014',
    'IXDSN.BFA': '013',
    'MAAD1.MAAD': '019',
    'MARC2.MARC': '016',
    'MARC3.MARC': '016',
    'METAL.BFA': '015',
    'NODEG.UG': '   ',  # leave null
    'PHOTO.BFA': '029',
    'PNTDR.BFA': '028',
    'PPMBA.MBA': '021',  # Public Policy MBA
    'PRECO': '   ',  # leave null, pre-college
    'PRINT.BFA': '030',
    'SCULP.BFA': '031',
    'SFMBA.MBA': '022',  # Strategic Finance MBA
    'TEXTL.BFA': '032',
    'UNDEC.BFA': '033',
    'VISCR.MA': '018',  # MA VCS
    'VISST.BA': '034',
    'WRITE.MFA': '027',
    'WRLIT.BA': '035'
}
