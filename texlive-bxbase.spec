# revision 28825
# category Package
# catalog-ctan /language/japanese/BX/bxbase
# catalog-date 2013-01-13 12:34:17 +0100
# catalog-license other-free
# catalog-version 0.5
Name:		texlive-bxbase
Version:	0.5
Release:	7
Summary:	BX bundle base components
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/BX/bxbase
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxbase.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxbase.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive bxbase package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bxbase/bxbase.def
%{_texmfdistdir}/tex/latex/bxbase/bxbase.sty
%{_texmfdistdir}/tex/latex/bxbase/bxucs.sty
%{_texmfdistdir}/tex/latex/bxbase/bxutf8.def
%{_texmfdistdir}/tex/latex/bxbase/bxutf8x.def
%{_texmfdistdir}/tex/latex/bxbase/zxbase.sty
%doc %{_texmfdistdir}/doc/latex/bxbase/00README
%doc %{_texmfdistdir}/doc/latex/bxbase/LICENSE
%doc %{_texmfdistdir}/doc/latex/bxbase/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
