%define	pdir	Algorithm
%define	pnam	Diff
%include	/usr/lib/rpm/macros.perl
Summary:	Algorithm-Diff perl module
Summary(pl):	Modu³ perla Algorithm-Diff
Name:		perl-Algorithm-Diff
Version:	1.10
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
%{perl_sitelib}/Algorithm/*.pm
