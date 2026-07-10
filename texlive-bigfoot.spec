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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

