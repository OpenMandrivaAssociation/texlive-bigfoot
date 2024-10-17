Name:		texlive-bigfoot
Version:	38248
Release:	2
Summary:	Footnotes for critical editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bigfoot
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bigfoot
%doc %{_texmfdistdir}/doc/latex/bigfoot
#- source
%doc %{_texmfdistdir}/source/latex/bigfoot

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
