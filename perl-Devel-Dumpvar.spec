
%define realname   Devel-Dumpvar
%define version    0.04
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A pure-OO reimplementation of dumpvar.pl
Source:     http://www.cpan.org/modules/by-module/Devel/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Spec)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*


