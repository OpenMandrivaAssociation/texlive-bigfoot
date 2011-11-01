Name:		texlive-bigfoot
Version:	20070813
Release:	1
Summary:	Footnotes for critical editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bigfoot
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package aims to provide a 'one-stop' solution to
requirements for footnotes. It offers: - Multiple footnote
apparatus superior to that of the manyfoot; - Footnotes can be
formatted in separate paragraphs, or be run into a single
paragraph (this choice may be selected per footnote series); -
Things you might have expected (like \verb-like material in
footnotes, and colour selections over page breaks) now work.
Note that the majority of the bigfoot package's interface is
identical to that of manyfoot; users should seek information
from that package's documentation. The bigfoot bundle also
provides the perpage and suffix packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bigfoot/bigfoot.sty
%{_texmfdistdir}/tex/latex/bigfoot/perpage.sty
%{_texmfdistdir}/tex/latex/bigfoot/suffix.sty
%doc %{_texmfdistdir}/doc/latex/bigfoot/README
%doc %{_texmfdistdir}/doc/latex/bigfoot/bigfoot.pdf
%doc %{_texmfdistdir}/doc/latex/bigfoot/perpage.pdf
%doc %{_texmfdistdir}/doc/latex/bigfoot/suffix.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bigfoot/bigfoot.drv
%doc %{_texmfdistdir}/source/latex/bigfoot/bigfoot.dtx
%doc %{_texmfdistdir}/source/latex/bigfoot/bigfoot.ins
%doc %{_texmfdistdir}/source/latex/bigfoot/perpage.drv
%doc %{_texmfdistdir}/source/latex/bigfoot/perpage.dtx
%doc %{_texmfdistdir}/source/latex/bigfoot/suffix.drv
%doc %{_texmfdistdir}/source/latex/bigfoot/suffix.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
