#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Algorithm
%define		pnam	Diff
Summary:	Algorithm::Diff - compute `intelligent' differences between two files / lists
Summary(pl.UTF-8):	Algorithm::Diff - ,,inteligentne'' znajdowanie różnic pomiędzy dwoma plikami / listami
Name:		perl-Algorithm-Diff
Version:	1.1902
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff3e17ae485f8adfb8857b183991fbce
URL:		http://search.cpan.org/dist/Algorithm-Diff/
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm::Diff finds differences between two files, two strings, or
any other two lists of things. It uses an intelligent algorithm
similar to (or identical to) the one used by the Unix `diff' program. 
It is guaranteed to find the *smallest possible* set of differences.

%description -l pl.UTF-8
Algorithm::Diff wyszukuje różnice pomiędzy dwoma plikami, łańcuchami
lub dwiema innymi listami. korzysta on z inteligentnego algorytmu
podobnego do (lub identycznego) używanego przez uniksowy program
,,diff''. Zagwarantowane jest znalezienie *najmniejszego możliwego*
zbioru różnic.

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
