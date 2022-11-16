Name:		texlive-latex2nemeth
Version:	64291
Release:	1
Summary:	Convert LaTeX source to Braille with math in Nemeth
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex2nemeth
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2nemeth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex2nemeth.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
After many failed attempts to transcribe real math notes and
books to Braille/Nemeth in order to deal with a real situation
(blind student in Math Dept.), we decided to develop a new
program that follows a direct, from LaTeX to Braille/Nemeth,
approach. Our main target was the Greek language which is only
Braille level 1, but English at level 1 is supported as well.
Simple pictures in PSTricks are also supported in order to
produce tactile graphics with specialized equipment. Note that
embossing will need LibreOffice and odt2braille as this project
does not deal with embossers' drivers. What's new in version
1.1 In this version, the support of the user level commands of
the amsmath package was added, as described in its user guide,
with the exception of commutative diagrams (amscd package) as
well as structures that are irrelevant to visually impared
persons. Also, the Unicode mathematics symbols of the
unicode-math package that are represented by the Nemeth code
are now supported by latex2nemeth. We would like to acknowledge
support by the TUGfund for this project (TUGfund project 33).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/latex2nemeth
%doc %{_texmfdistdir}/texmf-dist/doc/support/latex2nemeth

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
