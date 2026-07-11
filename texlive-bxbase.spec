%global tl_name bxbase
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2a
Release:	%{tl_revision}.1
Summary:	BX bundle base components
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxbase
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxbase.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxbase.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main purpose of this bundle is to serve as an underlying library for
other packages created by the same author (their names start with "BX"
or "PX"). However bxbase package contains a few user-level commands and
is of some use by itself.

