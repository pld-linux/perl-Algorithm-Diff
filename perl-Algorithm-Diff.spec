%include	/usr/lib/rpm/macros.perl
%define	pdir	Algorithm
%define	pnam	Diff
Summary:	Algorithm-Diff perl module
Summary(pl):	Modu� perla Algorithm-Diff
Name:		perl-Algorithm-Diff
Version:	1.10
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Algorithm-Diff finds differences between two files, two strings, etc.

%description -l pl
Algorithm-Diff wyszukuje r�nice pomi�dzy dwoma plikami, �a�cuchami,
itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_sitelib}/Algorithm/*.pm
