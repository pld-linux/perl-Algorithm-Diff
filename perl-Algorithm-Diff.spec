#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Algorithm
%define		pnam	Diff
Summary:	Algorithm::Diff perl module
Summary(pl):	Modu³ perla Algorithm::Diff
Name:		perl-Algorithm-Diff
Version:	1.15
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	457cd497a0411a88b47d3741eb176071
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::Diff finds differences between two files, two strings, etc.

%description -l pl
Algorithm::Diff wyszukuje ró¿nice pomiêdzy dwoma plikami, ³añcuchami,
itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{perl_vendorlib}/Algorithm/*.pl
%{perl_vendorlib}/Algorithm/*.pm
%{_mandir}/man3/*
