%include	/usr/lib/rpm/macros.perl
Summary:	Algorithm-Diff perl module
Summary(pl):	Modu³ perla Algorithm-Diff
Name:		perl-Algorithm-Diff
Version:	1.10
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/Algorithm-Diff-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm-Diff finds differences between two files, two strings, etc.

%description -l pl
Algorithm-Diff wyszukuje ró¿nice pomiêdzy dwoma plikami, ³añcuchami,
itp.

%prep
%setup -q -n Algorithm-Diff-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{perl_sitelib}/Algorithm
%attr(755,root,root) %{perl_sitelib}/Algorithm/*.pl
%{perl_sitearch}/auto/Algorithm/Diff
