%define upstream_name    Devel-Dumpvar
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A pure-OO reimplementation of dumpvar.pl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Most perl dumping modules are focused on serializing data structures into a
format that can be rebuilt into the original data structure. They do this
with a variety of different focuses, such as human readability, the ability
to execute the dumped code directly, or to minimize the size of the dumped
data.

Excect for the one contained in the debugger, in the file dumpvar.pl. This
is a much more human-readable form, highly useful for debugging, containing
a lot of extra information without the burden of needing to allow the dump
to be re-assembled into the original data.

The main downside of the dumper in the perl-debugger is that the dumpvar.pl
script is not really a readily loadable and useable module. It has
dedicated hooks from and to the debugger, and spans across multiple
namespaces, including main::.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2mdv2011.0
+ Revision: 653406
- rebuild for updated spec-helper

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 493486
- update to 1.06

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 401667
- rebuild using %%perl_convert_version
- fixed license field

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2010.0
+ Revision: 377989
- update to new version 1.05

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.04-1mdv2009.1
+ Revision: 329114
- import perl-Devel-Dumpvar


* Tue Jan 13 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

