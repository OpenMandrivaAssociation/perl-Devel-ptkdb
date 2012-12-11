
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




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.1091-2mdv2011.0
+ Revision: 654950
- rebuild for updated spec-helper

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.1091-1mdv2011.0
+ Revision: 375952
- import perl-Devel-ptkdb



