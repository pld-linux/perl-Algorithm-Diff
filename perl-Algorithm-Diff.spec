#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Algorithm
%define	pnam	Diff
Summary:	Algorithm::Diff - compute `intelligent' differences between two files / lists
Summary(pl):	Algorithm::Diff - ,,inteligentne'' znajdowanie ró¿nic pomiêdzy dwoma plikami / listami
Name:		perl-Algorithm-Diff
Version:	1.15
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	457cd497a0411a88b47d3741eb176071
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::Diff finds differences between two files, two strings, or
any other two lists of things.  It uses an intelligent algorithm
similar to (or identical to) the one used by the Unix `diff' program. 
It is guaranteed to find the *smallest possible* set of differences.

%description -l pl
Algorithm::Diff wyszukuje ró¿nice pomiêdzy dwoma plikami, ³añcuchami
lub dwiema innymi listami. korzysta on z inteligentnego algorytmu
podobnego do (lub identycznego) u¿ywanego przez uniksowy program
,,diff''. Zagwarantowane jest znalezienie *najmniejszego mo¿liwego*
zbioru ró¿nic.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{perl_vendorlib}/Algorithm/*.pl
%{perl_vendorlib}/Algorithm/*.pm
%{_mandir}/man3/*
