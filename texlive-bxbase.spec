Name:		texlive-bxbase
Version:	1.1
Release:	1
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
%{_texmfdistdir}/tex/latex/bxbase
%doc %{_texmfdistdir}/doc/latex/bxbase

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
