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
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
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
%attr(755,root,root) %{perl_sitelib}/Algorithm/*.pl
%{perl_sitelib}/Algorithm/*.pm
