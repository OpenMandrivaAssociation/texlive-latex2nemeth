%global tl_name latex2nemeth
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.3
Release:	%{tl_revision}.1
Summary:	Convert LaTeX source to Braille with math in Nemeth
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latex2nemeth
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2nemeth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2nemeth.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(latex2nemeth.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
After many failed attempts to transcribe real math notes and books to
Braille/Nemeth in order to deal with a real situation (blind student in
Math Dept.), we decided to develop a new program that follows a direct,
from LaTeX to Braille/Nemeth, approach. Our main target was the Greek
language which is only Braille level 1, but English at level 1 is
supported as well. Simple pictures in PSTricks are also supported in
order to produce tactile graphics with specialized equipment. Note that
embossing will need LibreOffice and odt2braille as this project does not
deal with embossers' drivers. What's new in version 1.1 In this version,
the support of the user level commands of the amsmath package was added,
as described in its user guide, with the exception of commutative
diagrams (amscd package) as well as structures that are irrelevant to
visually impaired persons. Also, the Unicode mathematics symbols of the
unicode-math package that are represented by the Nemeth code are now
supported by latex2nemeth. We would like to acknowledge support by TUG's
TeX development fund for this project (development fund project 33).

