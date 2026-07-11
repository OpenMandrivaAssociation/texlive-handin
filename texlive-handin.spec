%global tl_name handin
%global tl_revision 48255

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1
Release:	%{tl_revision}.1
Summary:	Light weight template for creating school submissions using LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/handin
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/handin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/handin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is for students creating school submissions using LaTeX. It
is especially suitable for math, physics, statistics and the like. It
can easily be used for creating exercises, too.

