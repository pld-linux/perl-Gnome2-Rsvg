#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pdir	Gnome2
%define		pnam	Rsvg
Summary:	Perl librsvg bindings
Summary(pl.UTF-8):	Wiązania librsvg dla Perla
Name:		perl-Gnome2-Rsvg
Version:	0.12
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7aea405c022ea2d531a83e210709dc88
Patch0:		%{name}-update.patch
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	librsvg-devel >= 2.16.0
BuildRequires:	perl-Cairo >= 1.00
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib >= 1.140
BuildRequires:	perl-Gtk2 >= 1.140
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	librsvg >= 2.16.0
Requires:	perl-Cairo >= 1.00
Requires:	perl-Glib >= 1.140
Requires:	perl-Gtk2 >= 1.140
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to librsvg library.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki librsvg.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gnome2-Rsvg bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2-Rsvg dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	librsvg-devel >= 2.16.0
Requires:	perl-Cairo-devel >= 1.00
Requires:	perl-Glib-devel >= 1.140
Requires:	perl-Gtk2-devel >= 1.140

%description devel
Development files for Perl Gnome2-Rsvg bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2-Rsvg dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Rsvg/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Rsvg.pm
%dir %{perl_vendorarch}/Gnome2/Rsvg
%dir %{perl_vendorarch}/auto/Gnome2/Rsvg
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Rsvg/Rsvg.so
%{_mandir}/man3/Gnome2::Rsvg*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Rsvg/Install
