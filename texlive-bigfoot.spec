%global tl_name bigfoot
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Footnotes for critical editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bigfoot
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bigfoot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package aims to provide a 'one-stop' solution to requirements for
footnotes. It offers: Multiple footnote apparatus superior to that of
manyfoot Footnotes can be formatted in separate paragraphs, or be run
into a single paragraph (this choice may be selected per footnote
series); Things you might have expected (such as \verb-like material in
footnotes, and colour selections over page breaks) now work. Note that
the majority of the bigfoot package's interface is identical to that of
manyfoot; users should seek information from that package's
documentation. The bigfoot bundle also provides the perpage and suffix
packages.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bigfoot
%dir %{_datadir}/texmf-dist/source/latex/bigfoot
%dir %{_datadir}/texmf-dist/tex/latex/bigfoot
%doc %{_datadir}/texmf-dist/doc/latex/bigfoot/COPYING
%doc %{_datadir}/texmf-dist/doc/latex/bigfoot/Makefile
%doc %{_datadir}/texmf-dist/doc/latex/bigfoot/README
%doc %{_datadir}/texmf-dist/doc/latex/bigfoot/bigfoot.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bigfoot/perpage.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bigfoot/suffix.pdf
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/bigfoot.drv
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/bigfoot.dtx
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/bigfoot.ins
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/perpage.drv
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/perpage.dtx
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/suffix.drv
%doc %{_datadir}/texmf-dist/source/latex/bigfoot/suffix.dtx
%{_datadir}/texmf-dist/tex/latex/bigfoot/bigfoot.sty
%{_datadir}/texmf-dist/tex/latex/bigfoot/perpage.sty
%{_datadir}/texmf-dist/tex/latex/bigfoot/suffix.sty
