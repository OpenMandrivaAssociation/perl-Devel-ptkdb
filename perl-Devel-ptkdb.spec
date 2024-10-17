%define realname   Devel-ptkdb

Name:		perl-%{realname}
Version:    1.1091
Release:    6
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl debugger using a Tk GUI
Source0:    Devel-ptkdb-1.1091.tar.gz
Url:		https://search.cpan.org/dist/%{realname}
BuildRequires: perl-devel
BuildArch: noarch

%description
Perl debugger using a Tk GUI 

%prep
%setup -q -n %{realname}-%{version} 

%build
yes | %{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}
