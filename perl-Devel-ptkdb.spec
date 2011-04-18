
%define realname   Devel-ptkdb

Name:		perl-%{realname}
Version:    1.1091
Release:    %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    DISTSUMMARY
Source0:    Devel-ptkdb-1.1091.tar.gz
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel



BuildArch: noarch

%description
DISTDESCR

%prep
%setup -q -n %{realname}-%{version} 

%build
yes | %{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}
%perl_vendorlib
#DISTEXTRA


