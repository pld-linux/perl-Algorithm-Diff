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
Version:	1.1903
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e8add21a641b8d66436df0c2024bf3b
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
%doc Changes README
%attr(755,root,root) %{perl_vendorlib}/Algorithm/cdiff.pl
%attr(755,root,root) %{perl_vendorlib}/Algorithm/diff.pl
%attr(755,root,root) %{perl_vendorlib}/Algorithm/diffnew.pl
%attr(755,root,root) %{perl_vendorlib}/Algorithm/htmldiff.pl
%{perl_vendorlib}/Algorithm/Diff.pm
%{perl_vendorlib}/Algorithm/DiffOld.pm
%{_mandir}/man3/Algorithm::Diff.3pm*
%{_mandir}/man3/Algorithm::DiffOld.3pm*
